class Shape:
    def draw(self, canvas):
        pass

class Point(Shape):
    def __init__(self, x, y):
        self.x, self.y = x,y

    def draw(self, canvas):
        r = 3
        canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill = "black")

class Segment(Shape):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas):
        canvas.create_line(self.start[0], self.start[1], self.end[0], self.end[1], width=3)

class Triangle(Shape):
    def __init__(self, points):
        self.points = points

    def draw(self, canvas):
        coords = []
        for p in self.points:
            if isinstance(p, Point):
#isinstance проверяет тип объекта. Если p — объект класса Point, то isinstance(p, Point) возвращает True.
                coords.extend([p.x, p.y])
            else:
                coords.extend(p)
        canvas.create_polygon(*coords, outline='red', fill= '', width=3)

class Polygone4(Shape):
    def __init__(self, points):
        self.points = points

    def draw(self, canvas):
        coords = []
        for p in self.points:
            if isinstance(p, Point):
#isinstance проверяет тип объекта. Если p — объект класса Point, то isinstance(p, Point) возвращает True.
                coords.extend([p.x, p.y])
            else:
                coords.extend(p)
        canvas.create_polygon(*coords, outline='green', fill= '', width=3)

class Cercle(Shape):
    def __init__(self, x, y, r):
        self.x, self.y = x,y
        self.r = r

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, outline="blue", fill = "", width=3)
