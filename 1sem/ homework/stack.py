# # 1 задание
# def remake_rpn(value: str):
#     vals = value.split()
#     stack = []
#     operators = {'+', '-', '*', '/'}
#
#     for val in vals:
#         if val.isdigit():
#             stack.append(int(val))
#         elif val in operators:
#             if len(stack) < 2:
#                 return None
#             b = stack.pop()
#             a = stack.pop()
#             if val == '+':
#                 stack.append(a + b)
#             elif val == '-':
#                 stack.append(a - b)
#             elif val == '*':
#                 stack.append(a * b)
#             elif val == '/':
#                 if b == 0:
#                     return None
#                 stack.append(a // b)
#         else:
#             return None
#
#     return stack[0] if len(stack) == 1 else None
#
# print(remake_rpn('2 3 *'))



#НАЧАЛО ПРОГРАММЫ 1 - 5 задания
from math import *

def remake_rpn(value: str, variables: dict):
    vals = value.split()
    stack = []
    binary_operators = {'+', '-', '*', '/'}
    unary_operators = {'neg', 'sqrt', 'sin', 'cos', 'tan', 'ctg', 'abs', 'log'}

    for val in vals:
        if val in variables:
            val = str(variables[val])

        try:
            number = float(val)
            stack.append(number)
            continue
        except ValueError:
            pass

        if val in binary_operators:
            if len(stack) < 2:
                return None
            b = stack.pop()
            a = stack.pop()
            if val == '+':
                stack.append(a + b)
            elif val == '-':
                stack.append(a - b)
            elif val == '*':
                stack.append(a * b)
            elif val == '/':
                if b == 0:
                    return None
                stack.append(a / b)

        elif val in unary_operators:
            if len(stack) < 1:
                return None
            a = stack.pop()
            if val == 'neg':
                stack.append(-a)
            elif val == 'sqrt':
                if a < 0:
                    return None
                stack.append(sqrt(a))
            elif val == 'sin':
                stack.append(sin(a))
            elif val == 'cos':
                stack.append(cos(a))
            elif val == 'tan':
                stack.append(tan(a))
            elif val == 'ctg':
                if sin(a) == 0:
                    return None
                stack.append(cos(a) / sin(a))
            elif val == 'abs':
                stack.append(abs(a))
            elif val == 'log':
                if a <= 0:
                    return None
                stack.append(log(a))
        else:
            return None

    return stack[0] if len(stack) == 1 else None

# print(remake_rpn("9 sqrt"))
# print(remake_rpn("3 log"))
# print(remake_rpn("4 neg abs"))
# print(remake_rpn("3.141592 cos"))



def remake_to_rpn(value: str, variables: dict):

    def is_number(val: str):
        try:
            float(val)
            return True
        except ValueError:
            return False

    vals = value.split()
    output_res = []
    stack = []

    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    func = {'sin', 'cos', 'tan', 'ctg', 'sqrt', 'neg', 'abs', 'log'}

    prev_token = None
    for val in vals:
        if val in variables:
            val = str(variables[val])

        if is_number(val):
            output_res.append(val)

        elif val in func:
            stack.append(val)

        elif val == '(':
            stack.append(val)

        elif val == ')':
            while stack and stack[-1] != '(':
                output_res.append(stack.pop())
            if not stack:
                return None
            stack.pop()
            if stack and stack[-1] in func:
                output_res.append(stack.pop())

        elif val in priority:
            if val == '-' and (prev_token in {None, '(', '+', '-', '*', '/'}):
                stack.append('neg')
            else:
                while (stack and stack[-1] != '(' and
                       (stack[-1] in func or priority.get(stack[-1], 0) >= priority[val])):
                    output_res.append(stack.pop())
                stack.append(val)
        else:
            return None
        prev_token = val

    while stack:
        if stack[-1] in {'(', ')'}:
            return None
        output_res.append(stack.pop())

    return ' '.join(output_res)


# print(remake_to_rpn("3 + 4 * 2"))
# print(remake_to_rpn("sin ( 0 )"))
# print(remake_to_rpn("3 * neg 4"))



def programm_rpn():
    print("Выберите режим:")
    print("1 — Преобразовать в RPN")
    print("2 — Вычислить выражение в RPN")
    print("3 — Преобразовать и вычислить")
    mode = input("Ваш выбор (1/2/3): ")

    variables = input_var()

    val = input("Введите выражение (после каждого символа ставьте пробел!!!): ")

    if mode == '1':
        rpn = remake_to_rpn(val, variables)
        print("RPN:", rpn if rpn is not None else "Ошибка при преобразовании.")
    elif mode == '2':
        result = remake_rpn(val, variables)
        print("Результат:", result if result is not None else "Ошибка при вычислении.")
    elif mode == '3':
        rpn = remake_to_rpn(val, variables)
        if rpn is None:
            print("Ошибка при преобразовании.")
        else:
            result = remake_rpn(rpn, variables)
            print("RPN:", rpn)
            print("Результат:", result if result is not None else "Ошибка при вычислении.")

    else:
        return None


#реализация ввода переменными
def input_var():
    variables = {}
    while True:
        var_input = input("Введите переменную (формат: x = 10) или 'стоп' для завершения: ")
        if var_input.lower() in ['стоп', 'cnjg', 'stop', 'ыещз']:
            break
        try:
            var_name, var_value = var_input.split('=')
            var_name = var_name.strip()
            var_value = var_value.strip()

            for func in ['log', 'sin', 'cos', 'tan', 'sqrt', 'abs']:
                var_value = var_value.replace(func, f"{func}")
            var_value = var_value.replace(" (", "(").replace(") ", ")")
            result = eval(var_value)
            variables[var_name] = result

        except ValueError:
            print("Некорректный ввод.")
            return None
    return variables


#запуск программы
programm_rpn()



