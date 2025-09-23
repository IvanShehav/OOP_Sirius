# tk_intersection_multilane.py
# Мультиполосная симуляция перекрестка с светофорами и предотвращением коллизий.
# Сохраните и запустите: python tk_intersection_multilane.py

import tkinter as tk
import random
import time

# ---------------- Модель: дорога, полоса, перекресток, машина, светофор ----------------

class TRoad:
    """Дорога как контейнер полос"""
    def __init__(self, length, orientation):
        assert orientation in ('h', 'v')
        self.length = float(length)
        self.orientation = orientation
        self.s_min = -self.length / 2.0
        self.s_max =  self.length / 2.0
        self.lanes = []  # список Lane

class Lane:
    """Одна полоса на дороге. direction: +1 или -1 (вдоль s). lateral_offset — для рисования"""
    def __init__(self, road, direction, lateral_offset):
        self.road = road
        self.direction = 1 if direction >= 0 else -1
        self.lateral_offset = lateral_offset
        # сантиметрическая длина полосы совпадает с дорогой
        self.s_min = road.s_min
        self.s_max = road.s_max

class Intersection:
    """Зона перекрёстка (по s-координате)."""
    def __init__(self, radius=2.0):
        self.radius = float(radius)
    def is_inside(self, s):
        return abs(s) < self.radius

class TCar:
    """
    Машина привязана к Lane, имеет координату s вдоль полосы.
    Для предотвращения коллизий учитывает только машины в своей полосе.
    """
    def __init__(self, lane, s0, speed, name='Car', color='gray'):
        self.lane = lane
        self.s = float(s0)
        self.v = float(speed)   # желательная скорость (ед./тик)
        self.name = name
        # физические габариты (в условных единицах, потом масштабируются)
        self.length = 2.0
        self.width  = 1.4
        self.color = color

    def xy_canvas(self, app):
        """Вернуть координаты центра в пикселях для рисования"""
        # s->x/y перевод: app центр (cx,cy)
        if self.lane.road.orientation == 'h':
            x = app.cx + self.s * app.scale
            y = app.cy + self.lane.lateral_offset * app.lane_spacing_px
        else:
            x = app.cx + self.lane.lateral_offset * app.lane_spacing_px
            # в логике s>0 = вверх, в canvas y уменьшается => invert
            y = app.cy - self.s * app.scale
        return x, y

    def distance_to_point_along_dir(self, point_s):
        """Положительная дистанция вдоль направления движения (учитывает цикличность полосы)."""
        delta = (point_s - self.s) * self.lane.direction
        if delta >= 0:
            return delta
        return delta + self.lane.road.length

    def distance_to_car_ahead(self, cars):
        """Ищем ближайшую машину впереди в той же полосе."""
        best = float('inf')
        best_car = None
        for other in cars:
            if other is self:
                continue
            if other.lane is not self.lane:
                continue
            d = self.distance_to_point_along_dir(other.s)
            if d < best:
                best = d
                best_car = other
        return best, best_car

    def move(self, cars, inter, traffic_controller, dt=1.0, safe_gap=1.2):
        """
        Движение с учётом:
         - машины впереди в той же полосе (не сближаемся меньше min_dist)
         - светофор (если перед въездом красный — останавливаться на стоп-линии)
         - если разрешено — въезжать в перекрёсток при зелёном (и если нет прямого конфликта с занятой зоной)
        """
        desired_step = self.v * dt

        # 1) учитывать машину впереди в полосе
        dist_ahead, car_ahead = self.distance_to_car_ahead(cars)
        if car_ahead is not None:
            min_dist = (self.length + car_ahead.length) / 2.0 + safe_gap
            allowed_step = max(0.0, dist_ahead - min_dist)
            if desired_step > allowed_step:
                desired_step = allowed_step

        # 2) стоп-линия и светофор
        # определяем точку входа в перекрёсток (entry_s)
        if self.lane.direction > 0:
            entry_s = -inter.radius
        else:
            entry_s = inter.radius

        dist_to_entry = self.distance_to_point_along_dir(entry_s)
        # расстояние, при котором мы считаем "мы у стоп-линии" (с учётом размера машины)
        stop_margin = self.length / 2.0 + safe_gap

        # должен ли машина останавливаться из-за светофора?
        light = traffic_controller.light_for_orientation(self.lane.road.orientation)
        # light.state in {'green', 'yellow', 'red'}
        must_stop_for_light = False
        if dist_to_entry <= desired_step + stop_margin:
            # мы могли бы пересечь стоп-линию на этом шаге
            if light.state == 'red':
                # остановиться перед стоп-линией (не заезжать)
                allowed_step_entry = max(0.0, dist_to_entry - stop_margin)
                if desired_step > allowed_step_entry:
                    desired_step = allowed_step_entry
                    must_stop_for_light = True
            elif light.state == 'yellow':
                # простая логика: если успеваем проехать полностью через перекресток — разрешаем,
                # иначе тормозим (зависит от скорости и расстояния)
                # здесь упростим: разрешаем въезд при желтом только если dist_to_entry < v*1.5
                if dist_to_entry > self.v * 1.5:
                    allowed_step_entry = max(0.0, dist_to_entry - stop_margin)
                    if desired_step > allowed_step_entry:
                        desired_step = allowed_step_entry
                        must_stop_for_light = True
            # если green — разрешено, но проверяем занятость перекрёстка с перпендикулярной дороги
            # (traffic_controller может дополнительно проверять, но мы сделаем двойную защиту ниже)

        # 3) предотвращение въезда, если перекрёсток занят перпендикулярной машиной
        # проверяем: собираемся ли въехать (быть внутри после шага)
        new_s = self.s + self.lane.direction * desired_step
        entering = (not inter.is_inside(self.s)) and inter.is_inside(new_s)
        if entering:
            perp_orientation = 'v' if self.lane.road.orientation == 'h' else 'h'
            # если есть машина в перекрестке с перпендикулярной ориентации — не въезжать
            if any(( (other.lane.road.orientation == perp_orientation) and inter.is_inside(other.s) ) for other in cars):
                # ограничиваем шаг так, чтобы остаться перед границей
                allowed_step_entry = max(0.0, dist_to_entry - stop_margin)
                if desired_step > allowed_step_entry:
                    desired_step = allowed_step_entry

        # применяем шаг
        self.s += self.lane.direction * desired_step

        # зацикливание по полосе
        if self.s > self.lane.road.s_max:
            self.s = self.lane.road.s_min + (self.s - self.lane.road.s_max)
        if self.s < self.lane.road.s_min:
            self.s = self.lane.road.s_max - (self.lane.road.s_min - self.s)


class TrafficLight:
    """Простой светофор для направления (ориентации дороги). Управляется TrafficController."""
    def __init__(self, orientation, green=6, yellow=2, red=8):
        self.orientation = orientation  # 'h' или 'v'
        self.green_dur = green
        self.yellow_dur = yellow
        self.red_dur = red
        self.state = 'red'
        self._time = 0

    def set_state(self, state):
        assert state in ('green','yellow','red')
        self.state = state

class TrafficController:
    """Координирует два светофора (горизонтальный и вертикальный) в простом цикле."""
    def __init__(self, h_light: TrafficLight, v_light: TrafficLight):
        self.h_light = h_light
        self.v_light = v_light
        # начнём с горизонтального зелёного
        self.cycle_time = 0
        self.current_phase = 0
        # phase sequence: (h_state, v_state, duration)
        self.phases = [
            ('green','red', self.h_light.green_dur),
            ('yellow','red', self.h_light.yellow_dur),
            ('red','green', self.v_light.green_dur),
            ('red','yellow', self.v_light.yellow_dur)
        ]
        self.phase_index = 0
        self.phase_elapsed = 0
        self.apply_phase()

    def apply_phase(self):
        h_state, v_state, dur = self.phases[self.phase_index]
        self.h_light.set_state(h_state)
        self.v_light.set_state(v_state)
        self.phase_elapsed = 0
        self.phase_duration = dur

    def tick(self):
        # увеличить таймер; при окончании фазы переход к следующей
        self.phase_elapsed += 1
        if self.phase_elapsed >= self.phase_duration:
            self.phase_index = (self.phase_index + 1) % len(self.phases)
            self.apply_phase()

    def light_for_orientation(self, orientation):
        return self.h_light if orientation == 'h' else self.v_light

# ---------------- GUI (Tkinter) и интеграция ----------------

class IntersectionApp:
    def __init__(self, master,
                 road_length=80.0,
                 lanes_each_dir=2,
                 scale=7.0,
                 canvas_size=700,
                 tick_ms=100,
                 auto_spawn=False):
        self.master = master
        self.canvas_size = canvas_size
        self.scale = scale
        self.tick_ms = tick_ms
        self.auto_spawn = auto_spawn
        self.spawn_counter = 0

        # центр и пиксели
        self.cx = canvas_size // 2
        self.cy = canvas_size // 2
        self.lane_spacing_px = 24  # пикселей между центрами полос

        # модель
        self.hroad = TRoad(road_length, 'h')
        self.vroad = TRoad(road_length, 'v')

        # создаём полосы (лево/право или вверх/вниз)
        # для горизонтали: положительные lateral_offset = вниз, отрицательные = вверх (для рисования)
        half = lanes_each_dir
        # горизонтальные: lanes for direction +1 (left->right) and -1 (right->left)
        offsets = []
        # arrange offsets so inner lanes are closer to center
        for i in range(half):
            offsets.append((i+0.5))
        # negative side
        for i in range(half):
            offsets.append(-(i+0.5))
        # assign alternating directions: for simplicity, first half direction +1, second half -1
        self.hroad.lanes = []
        for i, off in enumerate(offsets):
            direction = 1 if i < half else -1
            self.hroad.lanes.append(Lane(self.hroad, direction, off if direction==1 else -off))

        # vertical lanes: similar idea, but lateral_offset relative to x-axis
        offsets_v = []
        for i in range(half):
            offsets_v.append((i+0.5))
        for i in range(half):
            offsets_v.append(-(i+0.5))
        self.vroad.lanes = []
        for i, off in enumerate(offsets_v):
            direction = -1 if i < half else 1  # top->down negative, bottom->up positive (matching earlier code)
            self.vroad.lanes.append(Lane(self.vroad, direction, off if direction==1 else -off))

        self.inter = Intersection(radius=3.0)

        # светофоры
        self.h_light = TrafficLight('h', green=8, yellow=2)
        self.v_light = TrafficLight('v', green=8, yellow=2)
        self.traffic_controller = TrafficController(self.h_light, self.v_light)

        # машины
        self.cars = []
        self._create_initial_cars()

        # GUI
        self.canvas = tk.Canvas(master, width=canvas_size, height=canvas_size, bg='white')
        self.canvas.pack(side=tk.TOP)
        ctrl = tk.Frame(master)
        ctrl.pack(side=tk.BOTTOM, fill=tk.X)

        self.btn_start = tk.Button(ctrl, text="Start", command=self.start)
        self.btn_start.pack(side=tk.LEFT, padx=4, pady=4)
        self.btn_stop = tk.Button(ctrl, text="Stop", command=self.stop, state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=4, pady=4)
        self.btn_step = tk.Button(ctrl, text="Step", command=self.step_once)
        self.btn_step.pack(side=tk.LEFT, padx=4, pady=4)
        self.btn_add = tk.Button(ctrl, text="Add Car", command=self.add_random_car)
        self.btn_add.pack(side=tk.LEFT, padx=4, pady=4)
        self.auto_btn = tk.Button(ctrl, text="Auto Spawn: OFF", command=self.toggle_auto_spawn)
        self.auto_btn.pack(side=tk.LEFT, padx=4, pady=4)

        self.info_label = tk.Label(ctrl, text="")
        self.info_label.pack(side=tk.RIGHT, padx=8)

        self.road_items = []
        self.car_items = []
        self.light_items = {}

        self.running = False
        self._draw_static()
        self._draw_cars()
        self._draw_traffic_lights()

    def _create_initial_cars(self):
        colors = ['red','blue','green','orange','purple','brown','cyan','magenta']
        # create a few cars in various lanes
        for lane in self.hroad.lanes + self.vroad.lanes:
            # random chance to place a car on lane (not overcrowd)
            if random.random() < 0.35:
                # place either on left side (s negative) or right/top bottom random
                s0 = random.uniform(lane.road.s_min + 5, lane.road.s_max - 5)
                speed = random.uniform(1.0, 2.4)
                c = TCar(lane, s0, speed, name=f"C{len(self.cars)+1}", color=random.choice(colors))
                self.cars.append(c)

    def s_to_x(self, s):
        return self.cx + s * self.scale

    def s_to_y(self, s):
        return self.cy - s * self.scale

    def _draw_static(self):
        for it in self.road_items:
            self.canvas.delete(it)
        self.road_items.clear()

        wroad_px = self.lane_spacing_px * (len(self.hroad.lanes)/2 + 1.2)

        # horizontal band
        x0 = 0
        y0 = self.cy - wroad_px/2
        x1 = self.canvas_size
        y1 = self.cy + wroad_px/2
        r1 = self.canvas.create_rectangle(x0, y0, x1, y1, fill='#e6e6e6', outline='')
        self.road_items.append(r1)

        # vertical band
        x0 = self.cx - wroad_px/2
        y0 = 0
        x1 = self.cx + wroad_px/2
        y1 = self.canvas_size
        r2 = self.canvas.create_rectangle(x0, y0, x1, y1, fill='#e6e6e6', outline='')
        self.road_items.append(r2)

        # lane center lines (for visual)
        for lane in self.hroad.lanes:
            y = self.cy + lane.lateral_offset * self.lane_spacing_px
            it = self.canvas.create_line(0, y, self.canvas_size, y, dash=(3,5))
            self.road_items.append(it)
        for lane in self.vroad.lanes:
            x = self.cx + lane.lateral_offset * self.lane_spacing_px
            it = self.canvas.create_line(x, 0, x, self.canvas_size, dash=(3,5))
            self.road_items.append(it)

        # intersection border
        r = self.inter.radius * self.scale
        it = self.canvas.create_rectangle(self.cx - r, self.cy - r, self.cx + r, self.cy + r, outline='black', dash=(4,4))
        self.road_items.append(it)

    def _draw_traffic_lights(self):
        # draw small rectangles/circles near each approach
        size = 12
        offset = 10
        # horizontal approaches: left and right near center
        # left approach (cars coming rightwards) place traffic light at x = center - intersection.radius*scale - offset
        x_left = self.cx - int(self.inter.radius * self.scale) - offset
        y_left_up = self.cy - (self.lane_spacing_px * (len(self.hroad.lanes)/2)) - 20
        y_left_down = self.cy + (self.lane_spacing_px * (len(self.hroad.lanes)/2)) + 5

        # to simplify, we put one light for the whole horizontal direction (top-left of intersection)
        # horizontal light at left side (controls left->right and right->left)
        # We'll draw two small circles: one for horizontal (left side) and one for vertical (top side)
        # horizontal light (left of intersection)
        if 'h' in self.light_items:
            for it in self.light_items['h']:
                self.canvas.delete(it)
        hx = x_left
        hy = self.cy - int(self.inter.radius * self.scale) - offset
        # three circles for red/yellow/green stacked vertically
        items = []
        r = size
        items.append(self.canvas.create_oval(hx-r, hy-3*r, hx+r, hy-r, fill='gray'))   # red
        items.append(self.canvas.create_oval(hx-r, hy-r, hx+r, hy+r, fill='gray'))    # yellow
        items.append(self.canvas.create_oval(hx-r, hy+ r, hx+r, hy+3*r, fill='gray')) # green
        self.light_items['h'] = items

        # vertical light (top)
        if 'v' in self.light_items:
            for it in self.light_items['v']:
                self.canvas.delete(it)
        vx = self.cx + int(self.inter.radius * self.scale) + offset
        vy = self.cy - int(self.inter.radius * self.scale) - offset
        items_v = []
        items_v.append(self.canvas.create_oval(vx-r, vy-3*r, vx+r, vy-r, fill='gray'))   # red
        items_v.append(self.canvas.create_oval(vx-r, vy-r, vx+r, vy+r, fill='gray'))    # yellow
        items_v.append(self.canvas.create_oval(vx-r, vy+ r, vx+r, vy+3*r, fill='gray')) # green
        self.light_items['v'] = items_v

        self._update_light_graphics()

    def _update_light_graphics(self):
        # update color of drawn lights based on state
        def set_colors(items, state):
            # items: [red_circle, yellow_circle, green_circle]
            colors = {'red':'red','yellow':'yellow','green':'green'}
            self.canvas.itemconfig(items[0], fill = colors['red'] if state=='red' else 'gray')
            self.canvas.itemconfig(items[1], fill = colors['yellow'] if state=='yellow' else 'gray')
            self.canvas.itemconfig(items[2], fill = colors['green'] if state=='green' else 'gray')

        set_colors(self.light_items['h'], self.h_light.state)
        set_colors(self.light_items['v'], self.v_light.state)

    def _draw_cars(self):
        # delete old items
        for rect_id, text_id in self.car_items:
            self.canvas.delete(rect_id)
            self.canvas.delete(text_id)
        self.car_items.clear()

        for car in self.cars:
            rect, txt = self._draw_single_car(car)
            self.car_items.append((rect, txt))

    def _draw_single_car(self, car):
        x, y = car.xy_canvas(self)
        # convert size to px
        w = car.width * self.scale
        h = car.length * self.scale
        if car.lane.road.orientation == 'h':
            x0 = x - h/2
            x1 = x + h/2
            y0 = y - w/2
            y1 = y + w/2
        else:
            x0 = x - w/2
            x1 = x + w/2
            y0 = y - h/2
            y1 = y + h/2
        rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill=car.color, outline='black')
        txt = self.canvas.create_text(x1+6, y0-6, text=car.name, anchor='nw', font=('Arial', 9))
        return rect, txt

    def _update_car_graphics(self):
        # update coords of existing items
        for (rect_id, text_id), car in zip(self.car_items, self.cars):
            x, y = car.xy_canvas(self)
            w = car.width * self.scale
            h = car.length * self.scale
            if car.lane.road.orientation == 'h':
                x0 = x - h/2
                x1 = x + h/2
                y0 = y - w/2
                y1 = y + w/2
            else:
                x0 = x - w/2
                x1 = x + w/2
                y0 = y - h/2
                y1 = y + h/2
            self.canvas.coords(rect_id, x0, y0, x1, y1)
            self.canvas.coords(text_id, x1+6, y0-6)

    # ---------------- control / simulation loop ----------------

    def start(self):
        if not self.running:
            self.running = True
            self.btn_start.config(state=tk.DISABLED)
            self.btn_stop.config(state=tk.NORMAL)
            self._loop()

    def stop(self):
        self.running = False
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)

    def step_once(self):
        # advance controller and one tick
        self.traffic_controller.tick()
        for car in self.cars:
            car.move(self.cars, self.inter, self.traffic_controller, dt=1.0, safe_gap=1.2)
        self._update_all_graphics()

    def add_random_car(self):
        colors = ['red','blue','green','orange','purple','brown','cyan','magenta']
        # pick random lane and spawn near its s_min or s_max depending on direction
        lane = random.choice(self.hroad.lanes + self.vroad.lanes)
        if lane.direction > 0:
            s0 = lane.s_min + random.uniform(2.0, 8.0)
        else:
            s0 = lane.s_max - random.uniform(2.0, 8.0)
        speed = random.uniform(1.0, 2.6)
        c = TCar(lane, s0, speed, name=f"C{len(self.cars)+1}", color=random.choice(colors))
        # ensure it's not spawned too close to an existing car in that lane
        dist, ahead = c.distance_to_car_ahead(self.cars)
        if ahead is None or dist > (c.length + (ahead.length if ahead else 0))/2.0 + 2.0:
            self.cars.append(c)
            rect, txt = self._draw_single_car(c)
            self.car_items.append((rect, txt))
        else:
            # skip spawn if too crowded
            pass

    def toggle_auto_spawn(self):
        self.auto_spawn = not self.auto_spawn
        self.auto_btn.config(text=f"Auto Spawn: {'ON' if self.auto_spawn else 'OFF'}")

    def _maybe_auto_spawn(self):
        if not self.auto_spawn:
            return
        # небольшая вероятность добавить новую машину каждые N тиков
        if random.random() < 0.12:
            self.add_random_car()

    def _update_all_graphics(self):
        self._update_light_graphics()
        self._update_car_graphics()
        self.info_label.config(text=f"Cars: {len(self.cars)}  Phase: {self.traffic_controller.phase_index}")

    def _loop(self):
        if not self.running:
            return
        # advance traffic controller
        self.traffic_controller.tick()
        # move cars
        for car in self.cars:
            car.move(self.cars, self.inter, self.traffic_controller, dt=1.0, safe_gap=1.2)
        # maybe spawn
        self._maybe_auto_spawn()
        # graphics
        # if number of car items less than cars (spawned), create new items
        if len(self.car_items) < len(self.cars):
            for car in self.cars[len(self.car_items):]:
                rect, txt = self._draw_single_car(car)
                self.car_items.append((rect, txt))
        self._update_all_graphics()
        # schedule next tick
        self.master.after(self.tick_ms, self._loop)


def main():
    root = tk.Tk()
    root.title("Мультиполосный перекрёсток с светофорами (Tkinter)")
    app = IntersectionApp(root,
                          road_length=80.0,
                          lanes_each_dir=2,  # число полос в каждом направлении (можно поставить 1..3)
                          scale=7.0,
                          canvas_size=800,
                          tick_ms=120,
                          auto_spawn=False)
    root.mainloop()

if __name__ == '__main__':
    main()
