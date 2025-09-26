###РЕШЕНИЕ ЗАДАЧ ЕГЭ ИНФОРМАТИКА
# print("WXYZ")
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if ((x <= (z <= w)) and (z <= (y == (not w)))) == 0:
#                     print (w, x, y, z)


# mx = 0
# for n in range(1,13):
#     res = (str(bin(n)))[2:]
#     res_i = int(res)
#     if res_i % 2 == 0:
#         res = '10' + res
#     else:
#         res = '1' + res + '01'
#     res = int(res, 2)
#     mx = max(res, mx)
#
# print(mx)

# from turtle import *
# left(90)
# screensize(2000, 2000)
# tracer(0)
# k = 40
# pd()
#
# for i in range(7):
#     forward(10*k)
#     right(120)
#
# up()
# for x in range(-40,40):
#     for y in range(-40,40):
#         setpos(x*k, y*k)
#         dot(5, "red")
# done()

# # ЬЬЬРР
# num = '77755'
# res = int(num, 8)
# print(res+1)

from sys import *
setrecursionlimit(10**9)

# def f(n):
#     if n < 3:
#         return n
#     if n >= 3:
#         return (n-1) * f(n-2)
#
# print((f(2025)-f(2023))/f(2021))


# def f(x, end):
#     if x > end or x == 15:
#         return 0
#     if x == end:
#         return 1
#     return f(x+1, end) + f(x+3, end) + f(x*3, end)
# print(f(7,14) * f(14,20))

from fnmatch import *
for x in range(0, 10**10 +1, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x//1917)

from itertools import *
# cnt = 0
# for x in product('0123456789AB', repeat=5):
#     task = x.count('9') + x.count('A') + x.count('B')
#     if x.count('7') == 1 and task <= 3 and x[0] != '0':
#         cnt += 1
# print(cnt)


# s = '1' * 81
#
# while '11111' in s or '888' in s:
#     if '11111' in s:
#         s = s.replace('11111', '88', 1)
#     else:
#         s = s.replace('888', '8', 1)
# print(s)



# alph = '0123456789ABCDEFGHIJKLMNOPQRSTU'
# mx = 0
# for x in alph[::-1]:
#     s = (f'123{x}AB3')
#     s1 = (f'3CE{x}321')
#     s = int(s, 31)
#     s1 = int(s1,31)
#     res = s + s1
#     if res % 17 == 0:
#         print(res//17)
#         break


# for x in range(2030, 1, -1):
#     s = 7 ** 170 + 7 ** 100 - x
#     if str(s).count('0') == 71:
#         print(int(x, 7))
#         break

#
# cnt = 0
# while cnt != 5:
#     for i in range(800000, 1000000):
#         if i % 10 == 4:
#