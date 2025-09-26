import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
import os
from fpdf import FPDF
from matplotlib import rcParams
import numpy as np
from PIL import Image

rcParams['animation.embed_limit'] = 50

# Создание папки для анимаций
if not os.path.exists("animations"):
    os.makedirs("animations")

# =======================
# 📌 Реализации алгоритмов
# =======================

def bubble_sort(arr):
    steps = []
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            steps.append(a.copy())
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    steps.append(a.copy())
    return a, steps

def insertion_sort(arr):
    steps = []
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            steps.append(a.copy())
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    steps.append(a.copy())
    return a, steps

def selection_sort(arr):
    steps = []
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            steps.append(a.copy())
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    steps.append(a.copy())
    return a, steps

def merge_sort(arr):
    steps = []
    def merge(a, l, m, r):
        L = a[l:m]
        R = a[m:r]
        i = j = 0
        for k in range(l, r):
            if i < len(L) and (j >= len(R) or L[i] <= R[j]):
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            steps.append(a.copy())

    def divide(a, l, r):
        if r - l > 1:
            m = (l + r) // 2
            divide(a, l, m)
            divide(a, m, r)
            merge(a, l, m, r)

    a = arr.copy()
    divide(a, 0, len(a))
    return a, steps

def quick_sort(arr):
    steps = []
    a = arr.copy()

    def quicksort(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quicksort(a, low, pi - 1)
            quicksort(a, pi + 1, high)

    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            steps.append(a.copy())
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        steps.append(a.copy())
        return i + 1

    quicksort(a, 0, len(a) - 1)
    return a, steps

def heap_sort(arr):
    steps = []
    a = arr.copy()

    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[i] < a[l]:
            largest = l
        if r < n and a[largest] < a[r]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            steps.append(a.copy())
            heapify(n, largest)

    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        steps.append(a.copy())
        heapify(i, 0)
    steps.append(a.copy())
    return a, steps

def tim_sort(arr):
    steps = [arr.copy(), sorted(arr)]
    return sorted(arr), steps

# ============
# 🧩 Метаданные
# ============

algorithms = {
    "Bubble Sort": {"func": bubble_sort, "desc": "Простая сортировка, сравнивающая соседние элементы и меняющая их местами."},
    "Insertion Sort": {"func": insertion_sort, "desc": "Вставляет элементы на своё место в отсортированной части массива."},
    "Selection Sort": {"func": selection_sort, "desc": "Выбирает минимальный элемент и помещает его в начало."},
    "Merge Sort": {"func": merge_sort, "desc": "Рекурсивно делит массив и сливает отсортированные части."},
    "Quick Sort": {"func": quick_sort, "desc": "Выбирает опорный элемент и рекурсивно сортирует подмассивы."},
    "Heap Sort": {"func": heap_sort, "desc": "Преобразует массив в кучу и извлекает максимум по очереди."},
    "Tim Sort": {"func": tim_sort, "desc": "Гибридная сортировка, используемая в Python. Комбинирует Merge и Insertion."}
}

# ======================
# 🎥 Анимация сортировки
# ======================

def animate_sort(steps, name):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(steps[0])), steps[0], align="edge")
    ax.set_title(name)
    ax.set_ylim(0, max(steps[0]) * 1.1)

    def update_plot(frame):
        for rect, val in zip(bar_rects, steps[frame]):
            rect.set_height(val)

    anim = animation.FuncAnimation(fig, update_plot, frames=len(steps), repeat=False)
    gif_name = f"animations/{name.replace(' ', '_').lower()}.gif"
    anim.save(gif_name, writer="pillow", fps=10)
    plt.close()
    return gif_name

# 🖼 Конвертация первого кадра GIF в PNG
def gif_to_png(gif_path):
    im = Image.open(gif_path)
    im.seek(0)
    png_path = gif_path.replace(".gif", ".png")
    im.save(png_path)
    return png_path

# ========================
# 📈 Производительность
# ========================

def benchmark():
    sizes = [10, 100, 1000, 5000, 10000]
    results = {name: [] for name in algorithms}

    for size in sizes:
        base = [random.randint(1, 1000) for _ in range(size)]
        for name, meta in algorithms.items():
            func = meta["func"]
            arr = base.copy()
            start = time.time()
            func(arr)[0]
            end = time.time()
            results[name].append(end - start)

    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, label=name)
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение производительности алгоритмов сортировки")
    plt.legend()
    plt.grid(True)
    plt.savefig("performance_comparison.png")
    plt.close()

# ============
# 🧾 Генерация PDF
# ============

def generate_pdf(results):
    pdf = FPDF()
    pdf.add_page()

    # 👇 Регистрация шрифта
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font("DejaVu", "", 14)
    pdf.set_auto_page_break(auto=True, margin=15)

    for name, meta in algorithms.items():
        pdf.add_page()
        pdf.set_font("DejaVu", "", 14)
        pdf.cell(0, 10, name, ln=True)

        pdf.set_font("DejaVu", "", 11)
        pdf.multi_cell(0, 8, meta["desc"])
        pdf.ln(4)

        pdf.cell(0, 10, "Визуализация (кадр из анимации):", ln=True)
        gif_path = results[name]['gif']
        png_path = gif_to_png(gif_path)
        pdf.image(png_path, x=10, w=180)

    pdf.add_page()
    pdf.set_font("DejaVu", "", 14)
    pdf.cell(0, 10, "Сравнение производительности", ln=True)
    pdf.image("performance_comparison.png", x=10, w=180)

    pdf.output("full_sorting_report.pdf")

# ============
# 🚀 Запуск
# ============

if __name__ == "__main__":
    example = [random.randint(10, 100) for _ in range(30)]
    result_data = {}

    for name, meta in algorithms.items():
        print(f"🔄 {name}")
        sorted_arr, steps = meta["func"](example)
        gif_path = animate_sort(steps, name)
        result_data[name] = {"gif": gif_path}

    benchmark()
    generate_pdf(result_data)
    print("✅ Готово! PDF: full_sorting_report.pdf")
