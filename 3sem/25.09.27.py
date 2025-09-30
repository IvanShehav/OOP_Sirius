#пользователь вводит выражение из 2 задание ЕГЭ по информатике, при помощи ткинтера
# рисуется таблица истинности 2**4. Три кнопки есть, вывести строки где получилось 1, где 0, и все (F).
# на выходе готовая таблица
#
# 2 сценарий
#заполняем таблицу из задания, рисуем ее
#на выходе получается ответ на задание
# from itertools import *
#
# def f(w,x,y,z):
#     return (x or y) and 1-(y==z) and 1-w
#
# print('wxyz')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if f(w, x, y, z) == 1:
#                     print(w,x,y,z)
#
#
# for a,b,c,d in product((0,1),repeat=4):
#     t = ((1,a,1,b), (0,1,c,0), (d,1,1,0))
#     if len(set(t)) == 3:
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p,r))) for r in t] == [1,1,1]:
#                 print(''.join(p))

import tkinter as tk
from tkinter import messagebox
from Classes2709 import ExpressionEvaluator, TruthTable
from Classes2709_2 import EgeSolver

NUM_PARTIAL_ROWS = 3
NUM_VARS = 4
NUM_COLS_TASK2 = 5

class TruthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Логический Анализатор")

        self.truthtable = None

        tk.Label(root, text="Логическое выражение:").pack(pady=(10, 0))
        self.entry_expr = tk.Entry(root, width=100, font=("Arial", 14))
        self.entry_expr.insert(0, "(¬x ≡ z) → (y ≡ (w ∨ x))")
        self.entry_expr.pack(pady=(0, 10), padx=10)

        # Привязка Ctrl+V
        self.entry_expr.bind('<Control-v>', self.paste_content)
        self.entry_expr.bind('<Command-v>', self.paste_content)
        self.entry_expr.bind('<Shift-Insert>', self.paste_content)

        self.entry_expr.bind('<Return>', lambda event: self.show_base_filter(event))

        main_frame = tk.Frame(root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self._setup_task1_frame(main_frame)
        self._setup_task2_frame(main_frame)

        self.show_base_filter()

    def paste_content(self, event):
        widget = event.widget
        try:
            content = self.root.clipboard_get()

            try:
                widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
            except tk.TclError:
                pass
            widget.insert(tk.INSERT, content)
            self.show_base_filter()
        except tk.TclError:
            pass
        return "break"

    # --- Задание 1 ---

    def _setup_task1_frame(self, main_frame):
        table_frame = tk.Frame(main_frame, relief=tk.RIDGE, borderwidth=2)
        table_frame.pack(side="left", padx=10, pady=5, fill='both', expand=True)

        tk.Label(table_frame, text="ЗАДАНИЕ 1: Таблица Истинности", font=("Arial", 14, "bold")).pack(pady=5)

        btn_frame = tk.Frame(table_frame)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="РЕШИТЬ", command=self.show_base_filter, font=("Arial", 12, "bold"), bg='#F08080').pack(side="left", padx=5)

        tk.Button(btn_frame, text="Показать все (16 строк)", command=self.show_all, bg='#DDEEFF').pack(side="left", padx=5)
        tk.Button(btn_frame, text="F=1", command=lambda: self.show_filtered(1)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="F=0", command=lambda: self.show_filtered(0)).pack(side="left", padx=5)

        self.text_table = tk.Text(table_frame, width=30, height=20, font=("Consolas", 12), state=tk.DISABLED)
        self.text_table.pack(pady=5, fill='both', expand=True)

    def _build_table(self):
        expr = self.entry_expr.get()
        if not expr:
            raise ValueError("Выражение не может быть пустым.")
        evaluator = ExpressionEvaluator(expr)
        self.truthtable = TruthTable(evaluator)

    def show_all(self):
        self._execute_task1_action(lambda: self.truthtable.rows, clear_before=True)

    def show_filtered(self, val):
        self._execute_task1_action(lambda: self.truthtable.filter_rows(val), clear_before=True)

    def show_base_filter(self, event=None):
        def filter_func():
            base_val = self.truthtable.get_base_filter()
            rows = self.truthtable.filter_rows(base_val)
            self.text_table.config(state=tk.NORMAL)
            self.text_table.insert(tk.END, f"\n--- Показаны F={base_val} (меньшее количество) ---\n")
            self.text_table.config(state=tk.DISABLED)
            return rows

        self._execute_task1_action(filter_func, append_message=False, clear_before=True)

    def _execute_task1_action(self, filter_function, append_message=False, clear_before=False):
        try:
            self._build_table()
            rows = filter_function()
            self._display_rows(rows, self.text_table, append_message, clear_before)
        except Exception as e:
            self._display_error(self.text_table, str(e))

    def _display_rows(self, rows, text_widget, append=False, clear_before=False):
        text_widget.config(state=tk.NORMAL)
        if clear_before or not append:
             text_widget.delete("1.0", tk.END)
             text_widget.insert(tk.END, "w x y z | F\n")
             text_widget.insert(tk.END, "-"*15 + "\n")

        for r in rows:
            text_widget.insert(tk.END, f"{r}\n")

        text_widget.config(state=tk.DISABLED)

    def _display_error(self, text_widget, error_message):
        text_widget.config(state=tk.NORMAL)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, f"ОШИБКА:\n{error_message}")
        text_widget.config(state=tk.DISABLED)
        self._update_answer_task2("ОШИБКА")


    # --- Задание 2 ---

    def _setup_task2_frame(self, main_frame):
        solver_frame = tk.Frame(main_frame, relief=tk.RIDGE, borderwidth=2)
        solver_frame.pack(side="right", padx=10, pady=5, fill='both', expand=True)

        tk.Label(solver_frame, text="ЗАДАНИЕ 2: Решатель ЕГЭ №2", font=("Arial", 14, "bold")).pack(pady=5)
        tk.Label(solver_frame, text="Частичная Таблица (с F в последнем столбце)", justify=tk.LEFT).pack(anchor='w', padx=5)

        grid_frame = tk.Frame(solver_frame)
        grid_frame.pack(pady=5, padx=5)

        # Первая строка - для порядка переменных
        self.var_labels = []
        for j in range(NUM_VARS):
            lbl = tk.Label(grid_frame, text="?", font=("Consolas", 12, "bold"))
            lbl.grid(row=0, column=j, padx=5, pady=2)
            self.var_labels.append(lbl)
        tk.Label(grid_frame, text="F", font=("Consolas", 12, "bold")).grid(row=0, column=NUM_VARS, padx=5, pady=2)

        # Поля ввода
        self.entry_fields = []
        for i in range(NUM_PARTIAL_ROWS):
            row_entries = []
            for j in range(NUM_COLS_TASK2):
                entry = tk.Entry(grid_frame, width=3, font=("Consolas", 12), justify='center')
                entry.grid(row=i+1, column=j, padx=5, pady=2)
                row_entries.append(entry)
            self.entry_fields.append(row_entries)



        # Кнопки для решения и копирования
        btn_solve_frame = tk.Frame(solver_frame)
        btn_solve_frame.pack(pady=10)

        tk.Button(btn_solve_frame, text=">> НАЙТИ ПОРЯДОК ПЕРЕМЕННЫХ <<", command=self.solve_ege_problem, font=("Arial", 12, "bold"), bg='lightblue').pack(side="left", padx=5)

        tk.Button(btn_solve_frame, text="Копировать ответ", command=self.copy_answer_task2, bg='#C0C0C0').pack(side="left", padx=5)

        tk.Label(solver_frame, text="ОТВЕТ:").pack()
        self.text_answer = tk.Text(solver_frame, width=30, height=3, font=("Consolas", 16, "bold"), state=tk.DISABLED)
        self.text_answer.pack(pady=5, padx=5, fill='x')

    def _get_partial_input(self):
        input_rows = []
        for row_entries in self.entry_fields:
            row_data = [entry.get().strip() for entry in row_entries]
            input_rows.append(row_data)
        return input_rows

    def _fill_partial_input(self, filled_rows: list, permutation: str):
        for i, var_name in enumerate(permutation):
            self.var_labels[i].config(text=var_name)

        for i, row in enumerate(filled_rows):
            if i < NUM_PARTIAL_ROWS:
                for j in range(NUM_VARS):
                    val = row[j]
                    self.entry_fields[i][j].delete(0, tk.END)
                    self.entry_fields[i][j].insert(0, val)

    def solve_ege_problem(self):
        self._update_answer_task2("Вычисление...")
        try:
            self._build_table()

            solver = EgeSolver(self.truthtable)
            input_data = self._get_partial_input()

            permutations_list, filled_rows = solver.solve(input_data)

            if len(permutations_list) == 1:
                answer = f"ОТВЕТ:\n{permutations_list[0]}"
                if filled_rows:
                    self._fill_partial_input(filled_rows, permutations_list[0])
            elif len(permutations_list) == 0:
                answer = "ОТВЕТ:\nРешение не найдено."
            else:
                answer = f"ОТВЕТ:\nНайдено несколько вариантов: {', '.join(permutations_list)}"

            if len(permutations_list) != 1:
                for i in range(NUM_VARS):
                    self.var_labels[i].config(text="?")

            self._update_answer_task2(answer)

        except Exception as e:
            messagebox.showerror("Ошибка Решателя ЕГЭ", str(e))
            self._update_answer_task2("ОШИБКА РЕШЕНИЯ")

    def copy_answer_task2(self):
        try:
            answer_text = self.text_answer.get("1.0", tk.END).strip()
            if "ОТВЕТ:" in answer_text:
                final_answer = answer_text.split('\n')[-1].strip()
            else:
                final_answer = answer_text

            self.root.clipboard_clear()
            self.root.clipboard_append(final_answer)
        except Exception:
            pass

    def _update_answer_task2(self, text):
        self.text_answer.config(state=tk.NORMAL)
        self.text_answer.delete("1.0", tk.END)
        self.text_answer.insert(tk.END, text)
        self.text_answer.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TruthApp(root)
    root.mainloop()