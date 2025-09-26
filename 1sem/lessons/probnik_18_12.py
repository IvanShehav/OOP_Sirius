# print("w x y z")
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if (((w <= y) <= x) or (not z)) == 0:
#                     print(w,x,y,z)
# def f(n):
#     num = bin(n)[2:]
#     if n % 2 == 0:
#         num = '10' + num
#     else:
#         num = '1' + num + '01'
#     return int(num, 2)
#
# ls = []
#
# for n in range(12+1):
#     ls.append(f(n))
#
# print(max(ls))
import itertools
# from turtle import *
# k = 30
# left(90)
# tracer(0)
#
# pd()
# for i in range(9):
#     forward(22 * k)
#     right(90)
#     forward(6*k)
#     right(90)
# pu()
# forward(1*k)
# right(90)
# forward(5*k)
# left(90)
# pd()
# for i in range(9):
#     forward(53 * k)
#     right(90)
#     forward(75*k)
#     right(90)
# pu()
#
# screensize(2000, 2000)
# for x in range(-40, 40):
#     for y in range(-40, 40):
#         setpos(x*k, y*k)
#         dot(5, "red")
#
# done()

# from itertools import *
# cnt = 0
# for i in product('0123456789AB', repeat=5):
#     s = "".join(i)
#     if s[0] != '0':
#         if s.count('7') == 1:
#             if (s.count('9') + s.count('A') + s.count('B')) <= 3:
#                 cnt += 1
#
# print(cnt)
#


# s = '1' * 81
#
# while '11111' in s or '888' in s:
#     if '11111' in s:
#         s = s.replace('11111', '88', 1)
#     else:
#         s = s.replace('888', '8', 1)
# print(s)


# s = 3 * 3125**8 + 2 * 625**7 - 4*625**6 + 3*125**5 - 2 *25**4 - 2025
# ls = ''
# while s > 0:
#     ls += str(s%25)
#     s //= 25
# print(ls)
# print(ls.count('0'))


# for x in range(2030, 0, -1):
#     s = 7**170 + 7**100 - x
#     cnt = 0
#     while s > 0:
#         if s % 7 == 0:
#             cnt += 1
#         s //= 7
#     if cnt == 71:
#         print(x)
#         break

# from sys import *
#
# setrecursionlimit(10**9)
#
# def f(n):
#     if n == 1: return 1
#     if n > 1:
#         return (n-1) * f(n-1)
# print((f(2024) + 2 * f(2023))/f(2022))


def f(x, n):
    if x <= 19 or n > 2:
        return n == 2
    h = [f(x-2, n+1), f(x-5, n+1), f(x//3, n+1)]
    return all(h) if n % 2 == 0 else any(h)

for s in range(20, 1, -1):
    if f(s, 0):
        print(s)


# def f(start, end):
#     if start == end: return 1
#     if start < end: return 0
#     return f(start-2, end) + f(start // 2, end)
# print(f(38, 16) * f(16,2))


# for x in range(0,19):
#     a = 1 * 19**0 + 2*19**1 + x*19**2 + 7*19**3 + 9*19**4 + 8*19**5 + 8*19**6 + 9 * 19**7
#     b = 3*19**0 + 2*19**1 + 9*19**2 + x*19**3 + 2*19**4
#     if (a+b) % 18 == 0:
#         print(x//18)
#         break


# alph = '0123456789ABCDEFGH'
#
# for x in alph[::-1]:
#     res = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
#     if res % 18 == 0:
#         print(res//18)
#         break


# s = [int(s) for s in open('17.txt')]
# mn = min(x for x in s)
# res = []
# for i in range(len(s)-1):
#     if s[i] % 16 == mn or s[i+1] % 16 == mn:
#         res.append(s[i] + s[i+1])
# print(len(res))
# print(max(res))


# from fnmatch import *
#
# for x in range(0, 10**10+1, 1917):
#     if fnmatch(str(x), '3?12?14*5'):
#         print(x, x//1917)


cnt = 0
for i in range(800001, 100_000_000):
    m = 0
    a = []

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            a.append(j)
            b = i//j
            if j != b:
                a.append(b)
    if len(a) >= 1:
        a.sort()
        m = a[0] + a[-1]

        if m % 10 == 8:
            print(i,m)

            cnt += 1
            if cnt == 5:
                break

#
# ##24 задача егэ
# f = open('24_17878.txt')
# s = f.read()
# k, max1 = 0, 0
# for i in range(len(s)-1):
#     if (s[i] in '06789') or (s[i-1] in '6789' and s[i+1] in '6789' and k != 0):
#         k += 1
#     else:
#         max1 = max(max1,k)
#         k = 0
# print(max1)







