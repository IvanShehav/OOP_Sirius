# main.py
import tkinter as tk
from tkinter import simpledialog, messagebox, Frame, Label, Entry, Button, Text, Toplevel, Canvas, StringVar
from Classes0410 import GraphSolver, GraphVisualizer

class App(tk.Tk):
    def __init__(self, num_vertices):
        super().__init__()
        self.num_points = num_vertices
        self.title(f"Дороги (Задание 1) - {self.num_points}x{self.num_points}")

        self.entry_widgets = []
        self.solution_result = StringVar()
        self.solver_instance = None
        self._create_widgets()

    def _create_widgets(self):
        matrix_frame = Frame(self, padx=10, pady=10)
        matrix_frame.pack(side="left", fill="y", expand=True)

        for i in range(self.num_points + 1):
            row_entries = []
            for j in range(self.num_points + 1):
                if i == 0 and j > 0:
                    Label(matrix_frame, text=f"П{j}", font="Arial 10 bold").grid(row=i, column=j)
                elif j == 0 and i > 0:
                    Label(matrix_frame, text=f"П{i}", font="Arial 10 bold").grid(row=i, column=j)
                elif i > 0 and j > 0:
                    entry = Entry(matrix_frame, width=4, justify="center")
                    entry.grid(row=i, column=j, padx=1, pady=1)
                    if i == j:
                        entry.config(state="disabled", bg="#e0e0e0")
                    row_entries.append(entry)
            if i > 0:
                self.entry_widgets.append(row_entries)

        controls_frame = Frame(self, padx=10, pady=10)
        controls_frame.pack(side="right", fill="both", expand=True)

        Label(controls_frame, text="Опишите схему (каждая связь с новой строки):", anchor="w").pack(fill="x")
        self.graph_structure_text = Text(controls_frame, height=8, width=40)
        self.graph_structure_text.pack(fill="x", pady=(0, 10))
        self.graph_structure_text.insert("1.0", "Пример:\nА-Б\nБ-В\nВ-Г\nГ-А")

        target_frame = Frame(controls_frame)
        target_frame.pack(fill="x", pady=5)
        Label(target_frame, text="Найти длину из").pack(side="left")
        self.start_node_entry = Entry(target_frame, width=5)
        self.start_node_entry.pack(side="left")
        Label(target_frame, text="в").pack(side="left")
        self.end_node_entry = Entry(target_frame, width=5)
        self.end_node_entry.pack(side="left")

        Button(controls_frame, text="Решить", command=self.solve_task).pack(fill="x", pady=5)

        result_frame = Frame(controls_frame)
        result_frame.pack(fill="x", pady=5)
        Label(result_frame, text="Ответ:").pack(side="left")
        Entry(result_frame, textvariable=self.solution_result, state="readonly").pack(side="left", expand=True, fill="x")
        Button(result_frame, text="Копировать", command=self.copy_to_clipboard).pack(side="left", padx=5)

        Button(controls_frame, text="Нарисовать граф", command=self.draw_graph).pack(fill="x", pady=10)

    def get_matrix_from_entries(self):
        matrix = []
        for i in range(self.num_points):
            row = []
            for j in range(self.num_points):
                if i == j:
                    row.append(0)
                    continue
                val = self.entry_widgets[i][j].get()
                try:
                    row.append(int(val) if val else 0)
                except ValueError:
                    messagebox.showerror("Ошибка", f"Некорректное значение в ячейке ({i+1}, {j+1})")
                    return None
            matrix.append(row)
        return matrix

    def parse_structure(self):
        text = self.graph_structure_text.get("1.0", "end")
        graph_map = {}
        nodes = set()
        for line in text.splitlines():
            line = line.strip().upper()
            if not line or "ПРИМЕР" in line:
                continue
            if '-' not in line:
                continue
            parts = line.split('-')
            if len(parts) != 2:
                continue
            node1, node2 = parts[0].strip(), parts[1].strip()
            if not node1 or not node2:
                continue
            graph_map.setdefault(node1, []).append(node2)
            graph_map.setdefault(node2, []).append(node1)
            nodes.add(node1); nodes.add(node2)

        for node in nodes:
            graph_map.setdefault(node, [])

        if not graph_map:
            messagebox.showerror("Ошибка", "Не удалось распознать структуру схемы.")
            return None
        return graph_map

    def solve_task(self):
        matrix = self.get_matrix_from_entries()
        target_graph_map = self.parse_structure()
        if matrix is None or target_graph_map is None:
            return

        if len(matrix) != len(target_graph_map):
            messagebox.showerror("Ошибка", "Размер таблицы не совпадает с количеством вершин в схеме!")
            return

        self.solver_instance = GraphSolver(matrix, target_graph_map)
        if self.solver_instance.solve():
            start = self.start_node_entry.get().upper()
            end = self.end_node_entry.get().upper()
            if not start or not end:
                messagebox.showwarning("Внимание", "Введите начальную и конечную вершины.")
                return
            length = self.solver_instance.get_road_length(start, end)
            self.solution_result.set(str(length))
            messagebox.showinfo("Успех", "Решение найдено!")
        else:
            self.solution_result.set("Error")
            messagebox.showerror("Ошибка", "Не удалось найти решение. Проверьте данные.")

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.solution_result.get())

    def draw_graph(self):
        if not self.solver_instance or not self.solver_instance.solution_mapping:
            messagebox.showwarning("Внимание", "Сначала нужно найти решение.")
            return

        graph_window = Toplevel(self)
        graph_window.title("Итоговый граф")
        canvas = Canvas(graph_window, bg="white", width=600, height=500)
        canvas.pack(fill="both", expand=True)
        graph_window.update_idletasks()

        visualizer = GraphVisualizer(canvas, self.solver_instance.solution_mapping, self.solver_instance.matrix)
        visualizer.draw()
        canvas.bind("<Configure>", lambda e: visualizer.draw())


if __name__ == "__main__":
    root = tk.Tk(); root.withdraw()
    num_v = simpledialog.askinteger("Размер задачи", "Введите количество вершин в графе:", parent=root, minvalue=2, maxvalue=20)
    root.destroy()
    if num_v:
        app = App(num_v)
        app.mainloop()
