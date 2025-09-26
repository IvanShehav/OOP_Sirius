import tkinter as tk
from tkinter import messagebox
from periodictable import elements
import re

def calculate_molar_mass(formula):
    """Функция для вычисления молярной массы по формуле"""
    try:
        # Автоматически исправляем регистр в формуле
        corrected_formula = ''.join([char.upper() if i == 0 or formula[i - 1].isdigit() else char.lower() for i, char in enumerate(formula)])
        total_mass = 0.0

        # Разбиваем формулу на элементы и их количества
        pattern = re.compile(r"([A-Z][a-z]?)(\d*)")
        matches = pattern.findall(corrected_formula)

        for match in matches:
            symbol, count = match
            count = int(count) if count else 1
            element = getattr(elements, symbol)
            total_mass += element.mass * count

        return total_mass
    except AttributeError as e:
        messagebox.showerror("Ошибка", f"Не найден элемент в формуле: {e}")
        return None

def on_calculate():
    """Обработчик кнопки 'Вычислить'"""
    formula = entry.get().strip()
    if not formula:
        messagebox.showwarning("Предупреждение", "Введите формулу вещества!")
        return

    result = calculate_molar_mass(formula)
    if result is not None:
        result_label.config(text=f"Молярная масса: {result:.4f} г/моль")

# Создание графического интерфейса
root = tk.Tk()
root.title("Калькулятор молярной массы")
root.geometry("400x250")

# Инструкция для пользователя
instruction_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
instruction_frame.pack(fill=tk.X, padx=10, pady=10)
instruction_label = tk.Label(instruction_frame, text="Введите формулу вещества (например, H2O, NaCl, C6H12O6):\n"
                                                     "1. Используйте стандартные обозначения элементов.\n"
                                                     "2. Не используйте пробелы.\n"
                                                     "3. Не обращайте внимания на регистр (NaCl и nacl оба работают).",
                             bg="#f0f0f0", justify=tk.LEFT)
instruction_label.pack()

# Поле ввода формулы
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill=tk.X, padx=10, pady=10)
label = tk.Label(input_frame, text="Формула вещества:")
label.pack()
entry = tk.Entry(input_frame, width=30)
entry.pack(pady=5)

# Кнопка и метка для вывода результата
button_frame = tk.Frame(root, padx=10, pady=10)
button_frame.pack(fill=tk.X, padx=10, pady=10)
button = tk.Button(button_frame, text="Вычислить", command=on_calculate)
button.pack()
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Запуск приложения
root.mainloop()