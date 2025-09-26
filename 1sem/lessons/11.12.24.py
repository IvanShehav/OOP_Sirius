# def f(n):
#     number = bin(n)[2:]
#     if n % 2 == 0:
#         number = number + '00'
#     else:
#         number = number + '11'
#     return int(number, 2)
#
# for n in range(500, 1, -1):
#     if f(n) < 134:
#         print(n)
#         break
#
## 2 задание
# def f(n):
#     number = str(n)
#     sum = []
#     sum.append(number[0] + number[1])
#     sum.append(number[1] + number[2])
#     sum.append(number[2] + number[3])
#     a = sum[0]
#     b = sum[1]
#     c = sum[2]
#     sum.remove(min(sum))
#     sum.sort()
#     return sum[0] + sum[1]
# for i in range(1000,9999+1):
#     if f(i) == '1330':
#         print(i)
#         break

# a = ['1214', '1211', '9090']
# print(min(a))
import functools
# # 3 задание
# def f(x,y):
#     return ((2*x + 3*y  != 60) or (a >= x) or (a >= y))
#
# for a in range(0, 1000):
#     if all(f(x,y) for x in range(100) for y in range(100)):
#         print(a)
#         break

#4 задание
# m = 0
# P = [i for i in range(5, 31)]
# Q = [i for i in range(14, 24)]
# for Amin in range(1, 101):
#     for Amax in range(Amin + 1, 101):
#         check = 1
#         A = [i for i in range(Amin, Amax)]
#         for x in range(1, 101):
#             f = ((x in P) == (x in Q)) <= (not(x in A))
#             if not f:
#                 check = 0
#                 break
#         if check == 1:
#             m = max(m, Amax - Amin)
# print(m)
#5 задание
# from sys import *
# setrecursionlimit(10**9)
# from functools import *
# @functools.lru_cache(maxsize=1000)
# def f(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 != 0:
#         return f(n-1) + 3 * f(n-2)
#     if n > 2 and n % 2 == 0:
#         return sum(f(i) for i in range(1,n))
# print(f(28))
# #6 задание
# def f(n):
#     if n == 1: return n
#     if n > 1: return 2*f(n-1) + 1
# print(f(6))
#7 задание
# def f(x, n):
#     if x >= 74 or n > 2: return n == 2
#     h = [f(x+1, n+1), f(x+2, n+1), f(x*3, n+1)]
#     if x % 2 == 0:
#         return any(h)
#     else:
#         return any(h)
#
# for s in range(1, 73+1):
#     if f(s, 0):
#         print(s)
#         break

#8 задание
# def f(x, n):
#     if x >= 74: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(x+1, n-1), f(x+2, n-1), f(x*3, n-1)]
#     return any(h) if n % 2 != 0 else all(h)
# print([s for s in range(1 , 73+1) if not f(s, 1) and f(s,3)])

##9 задача
# def f(x, n):
#     if x >= 74 or n > 4: return n == 2 or n == 4
#     h = [f(x+1, n+1), f(x+2, n+1), f(x*3, n+1)]
#     if x % 2 == 0:
#         return any(h)
#     else:
#         return all(h)
#
# for s in range(1, 73+1):
#     if f(s, 0):
#         print(s)


#задача 13

# def f(a,b):
#     if a > b:
#         return 0
#     if a == b:
#         return 1
#     return f(a+1,b) + f(a*2, b)
#
# cnt = 0
# print(f(1,10)*f(10,21))

#задача 14

