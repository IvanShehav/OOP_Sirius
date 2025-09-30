from itertools import permutations, product
# Импортируем TruthTable, убедитесь, что он доступен
from Classes2709 import TruthTable

class EgeSolver:
    # Решает задачу ЕГЭ №2 (нахождение порядка переменных)
    def __init__(self, truthtable: TruthTable):
        self.truthtable = truthtable
        self.variables = ('w', 'x', 'y', 'z')
        # Для удобства храним только те строки, где F=1 (или F=0, в зависимости от фильтра)
        self.all_calculated_rows = truthtable.rows

    def parse_partial_table(self, input_rows: list) -> list:
        # Преобразует ввод (4 переменные + 1 F) в шаблон
        parsed_rows = []
        for row_data in input_rows:
            # Проверяем, что в строке 5 элементов
            if len(row_data) != 5:
                continue

            # Проверяем F: последний элемент
            f_val = row_data[4].strip()
            if f_val not in ('0', '1'):
                # Пропускаем пустые или невалидные строки, если F не задано
                continue

            partial_vars = []
            # Обрабатываем первые 4 (переменные)
            for val in row_data[:4]:
                val = val.strip()
                if val == '0':
                    partial_vars.append(0)
                elif val == '1':
                    partial_vars.append(1)
                elif val == '':
                    partial_vars.append('-') # Неизвестное
                else:
                    raise ValueError(f"Некорректное значение '{val}'. Используйте 0, 1 или оставьте пустым.")

            # Добавляем F как 5-й элемент
            partial_vars.append(int(f_val))
            parsed_rows.append(partial_vars)

        return parsed_rows

    def match_row(self, partial_row: list, full_row_dict: dict, full_row_f: int, permutation: tuple) -> bool:
        # Проверяет совпадение F
        partial_f = partial_row[4]
        if partial_f != full_row_f:
            return False

        # Проверяет совпадение переменных
        for i in range(4):
            partial_val = partial_row[i]
            variable_name = permutation[i] # Имя переменной в этом столбце
            full_val = full_row_dict[variable_name] # Значение этой переменной в полной таблице

            if partial_val != '-' and partial_val != full_val:
                return False

        return True

    def fill_row(self, full_row_tuple: tuple, permutation: tuple) -> tuple:
        # Заполняет '-' значения в шаблоне, используя полную строку и перестановку.
        # full_row_tuple: (w, x, y, z) - значения переменных

        # Создаем карту: {имя переменной: значение} для текущей полной строки
        full_map = dict(zip(self.variables, full_row_tuple))

        # Создаем заполненную строку в порядке перестановки (для отображения в интерфейсе)
        filled_row = [str(full_map[var_name]) for var_name in permutation]

        return tuple(filled_row)

    def solve(self, input_rows: list):
        # Основной решатель
        partial_rows = self.parse_partial_table(input_rows)
        if not partial_rows:
            return [], []

        num_partial = len(partial_rows)

        # Отфильтруем полную таблицу, используя F из первой строки частичной таблицы
        target_f = partial_rows[0][4]
        # Используем только те строки из полной таблицы, которые соответствуют F
        filtered_rows = self.truthtable.filter_rows(target_f)
        num_calculated = len(filtered_rows)

        solutions = {} # {перестановка: [заполненные строки]}

        # Индексы отфильтрованной таблицы
        full_indices = list(range(num_calculated))

        for p in permutations(self.variables):
            for combination in product(full_indices, repeat=num_partial):
                if len(set(combination)) != num_partial:
                    continue # Строки полной таблицы должны быть уникальны

                is_valid_mapping = True
                current_filled_rows = []

                for partial_index, calculated_index in enumerate(combination):
                    # Берем строку из отфильтрованной таблицы
                    full_row_obj = filtered_rows[calculated_index]

                    full_row_dict = full_row_obj.get_values()
                    full_row_f = full_row_obj.f
                    full_row_tuple = full_row_obj.get_vars_tuple()

                    partial_row_data = partial_rows[partial_index] # 4 vars + F

                    if not self.match_row(partial_row_data, full_row_dict, full_row_f, p):
                        is_valid_mapping = False
                        break

                    # Если совпало, заполняем пропуски для интерфейса
                    filled = self.fill_row(full_row_tuple, p)
                    current_filled_rows.append(filled)

                if is_valid_mapping:
                    perm_str = "".join(p)
                    if perm_str not in solutions:
                        solutions[perm_str] = current_filled_rows

        return list(solutions.keys()), solutions.get(next(iter(solutions), None))