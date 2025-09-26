# def final_price(price, discount=1):
#     return price - price*discount/100

# def value(x, list_arg=None): ## None не содержит значения, константа обозначающая пустоту
#     if list_arg is None:
#         list_arg = []
#     list_arg += [x]
#     return list_arg
#
# print(value(0))
# print(value(0, [1,2,3]))
# print(value(1))

##АРГУМЕНТЫ
# def final_price(price, discount=1):
#     return 0
# # - Позиционные (f(a,b) - f(5,4)
# print(final_price(1000, discount=5))
# # - Именнованные (обращение по имени)
# print(final_price(discount=5, price = 1000))

# def price(*price, disc=1):
#     return [prices - prices * disc / 100 for prices in price]
#
# print(price(100,200,300,disc=5))


# #Чтобы ввести колько угодно значений в именованный аргумент  - используем две звездочки
# def f_price(*prices, discount = 1, **kwargs):
#     low = kwargs.get('price_low', min(prices))
#     high = kwargs.get('price_high', max(prices))
#     return [price - price * discount / 100 for price in prices if low <= price <= high]
# print(f_price(100,200,300,400,500, discount=5, price_low=200, price_high=400))



##Функция высшего порядка. Функции, которые принимают аргументы функций.
#Функция filter() позволяет отбирать аргменты по критерию. Пример: отфильтровать список только по четным элементам
# def only_pos(x):
#     return x > 0
#
# res = filter(only_pos, [-1,5,6,-10,0])
# print(", ".join(str(x) for x in res))

# res = filter(str.isalpha, '123ABcd()')
# print("".join(res))

# def square(x):
#     return x **2
#
# res = map(square, range(5))
# print(", ".join(str(x) for x in res))


##Лямбда-функция. Может принимать огромное количество аргументов, но может вернуть только одино значене

# lambda x: x > 0
# res = filter(lambda x: x >0, [-1,5,6,-10,0])
# print(",".join(str(x) for x in res))

#Функция sorted()

# lines = ['abcd', 'ab', 'abc', 'abcdef']
# print(sorted(lines, key=lambda line: len(line)))



# lines = ['abcd', 'ab', 'abc', 'abcdef']
# print(sorted(lines, key = lambda  line: (-line), line))


# def  make_matrix(size, value = 0):
#     x, y = 0, 0
#     if type(size) == int:
#         x = size
#         y = size
#     else:
#         x = size[0]
#         y = size[1]
#     return [[value for _ in range(x)] for _ in range(y)]
#
# print(make_matrix(3))


# def gcd(*numbers):
#     a = list(numbers)
#     while len(a) > 1:
#         while a[1]:
#             a[0], a[1] = a[1], a[0] % a[1]
#         a.pop(1)
#     return a[0]

def to_string(*lines, sep = " ", end = "\n"):
    res = sep.join(str(line) for line in lines)
    return res + end
