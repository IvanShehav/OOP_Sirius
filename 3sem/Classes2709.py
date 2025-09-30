import re
from itertools import product
from collections import Counter

class ExpressionEvaluator:
    def __init__(self, expr_text: str):
        self.original_expr = expr_text.strip()

        s = self._guarantee_unicode_replacement(self.original_expr)

        self.expr_text = self._replace_implications_recursively(s)

    def _guarantee_unicode_replacement(self, expr: str) -> str:
        s = expr

        # 0. Максимальная очистка: Удаляем все невидимые пробелы и типографские символы
        s = s.replace('\u202f', ' ').replace('\u00a0', ' ').replace('\u2009', ' ')
        s = s.replace('\u00ad', ' ').replace('\u200b', ' ').replace('\u0020', ' ')

        # 1. Замены логических символов на Python-операторы
        s = s.replace("¬", " not ").replace("~", " not ").replace("!", " not ")
        s = s.replace("→", "->").replace("=>", "->")
        s = s.replace("∨", " or ").replace("\\/", " or ")
        s = s.replace("∧", " and ").replace("/\\", " and ")

        # 2. Замена Эквивалентности с гарантированными пробелами
        s = s.replace("≡", " == ")
        s = s.replace("==", " == ")

        # 3. Нормализация пробелов: удаляем двойные пробелы
        while '  ' in s:
            s = s.replace('  ', ' ')

        return s.strip()

    def _replace_implications_recursively(self, s: str) -> str:
        import re

        # Шаг 1: Гарантируем пробелы вокруг операторов для чистого поиска
        s = s.replace("->", " -> ").replace("==", " == ").replace(" and ", " and ").replace(" or ", " or ")
        while '  ' in s:
            s = s.replace('  ', ' ')

        if "->" not in s:
            return s.strip()

        # Шаг 2: Ищем шаблон (A) -> (B) или A -> B и заменяем на ((not A) or B)

        def replace_impl(match):
            A = match.group(1).strip()
            B = match.group(2).strip()
            return f'( (not {A}) or {B} )'

        # Паттерн ищет левую часть (группа 1) и правую часть (группа 2),
        # которые могут быть: переменной/not-выражением/выражением в скобках.
        pattern = re.compile(
            r'([A-Za-z]\b|not\s*\w+|\([^()]*\))\s*->\s*([A-Za-z]\b|not\s*\w+|\([^()]*\))'
        )

        s_temp = s

        # Выполняем замену до тех пор, пока '->' существуют
        while '->' in s_temp:
            new_s = re.sub(pattern, replace_impl, s_temp)

            if new_s == s_temp:
                # Если шаблон не сработал
                new_s = re.sub(r'(\w+)\s*->\s*(\w+)', replace_impl, s_temp)
                if new_s == s_temp:
                    # Если и это не помогло, значит, скобки расставлены неверно для парсера
                    raise ValueError(f"Ошибка парсинга импликации. Проверьте скобки в: {self.original_expr}")

            s_temp = new_s

        s = s_temp

        # Убираем лишние пробелы и возвращаем результат
        while '  ' in s:
            s = s.replace('  ', ' ')

        return s.strip()

    def evaluate(self, w, x, y, z):
        names = {'w': bool(w), 'x': bool(x), 'y': bool(y), 'z': bool(z)}
        try:
            val = eval(self.expr_text, {}, names)
        except Exception as e:
            raise ValueError(f"Ошибка вычисления: {e}")
        return int(bool(val))


class TruthRow:
    def __init__(self, w, x, y, z, f):
        self.w, self.x, self.y, self.z, self.f = w, x, y, z, f
    def __repr__(self):
        return f"{self.w} {self.x} {self.y} {self.z} | {self.f}"

    def get_values(self):
        return {'w': self.w, 'x': self.x, 'y': self.y, 'z': self.z}

    def get_vars_tuple(self):
        return (self.w, self.x, self.y, self.z)


class TruthTable:
    def __init__(self, evaluator: ExpressionEvaluator):
        self.evaluator = evaluator
        self.rows = []
        self.build_all()
        self.counts = Counter(r.f for r in self.rows)

    def build_all(self):
        self.rows = []
        for w, x, y, z in product((0,1), repeat=4):
            f = self.evaluator.evaluate(w,x,y,z)
            self.rows.append(TruthRow(w,x,y,z,f))

    def filter_rows(self, value=None):
        return [r for r in self.rows if r.f == value]

    def get_base_filter(self) -> int:
        count_0 = self.counts.get(0, 0)
        count_1 = self.counts.get(1, 0)
        return 0 if count_0 < count_1 else 1