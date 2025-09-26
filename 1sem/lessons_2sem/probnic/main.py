# print('w x y z F')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if ((x <= y) and z and not(w)) == 1:
#                     print(w,x,y,z)
#
# # xzyw

# #задача 5
#
# def sumNum(num):
#     cnt = 0
#     while num > 0:
#         cnt += num % 10
#         num = num // 10
#     return cnt % 2
# def f(n):
#     delit = n % 4
#     res = n - delit
#     res = bin(res)[2:]
#     res = res + str(sumNum(int(res)))
#     res = res + str(sumNum(int(res)))
#     return int(res, 2)
# for i in range(600, 1, -1):
#     if f(i) < 64:
#         print(i)
#         break
#отв 15

#задача 6
#
# from turtle import *
# left(90)
# screensize(2000, 2000)
# k = 20
# tracer(0)
#
# down()
# right(180)
# forward(2*k)
# right(90)
# forward(30*k)
# right(90)
# forward(2*k)
# right(30)
# for i in range(6):
#     forward(5*k)
#     right(120)
#     forward(5*k)
#     right(240)
# up()
#
# for x in range(-40, 20):
#     for y in range(-40, 20):
#         goto(x*k, y*k)
#         dot(5,'red')
#
# done()
#101

# #задача 8
# from itertools import *
# cnt = 0
#
# for i in product('0123', repeat=3):
#     s = ''.join(i)
#     if s[0] >= s[1] >= s[2]:
#         print(s)
#         cnt += 1
# print(cnt)
# #20

#
# #задание 12
# s = '1' * 91
# while '2222' in s or '1111' in s:
#     if '2222' in s:
#         s = s.replace('2222', '11', 1)
#     else:
#         s = s.replace('1111', '22', 1)
# print(s)
# #22111

# #задача 14
#
# s = 4**700 + 4**100 - 16**100 - 64
# cnt = 0
# res = ''
# while s > 0 :
#    res = str(s % 4) + res
#    s //= 4
# print(res)
# print(res.count('3'))
# #597

# #Задача 15
# def f(n, m):
#     return n % m == 0
#
# for a in range(1000, 1, -1):
#     flag = True
#     for x in range(1, 1000):
#         flag *= (not(f(x,a)) <= (f(x,24) <= (not(f(96,x)))))
#     if flag:
#         print(a)

# #задание 16
# from sys import *
# setrecursionlimit(10**8)
# def f(n):
#     if n == 1: return 1
#     if n % 2 == 0: return n + f(n-1)
#     if n > 1 and n % 2 != 0: return 2 * f(n-1) + f(n-2)
# print(f(20))
# #78731

#задание 19

# def f(a, b, n):
#     if a + b >= 122: return n % 2
#     if n < 0: return 0
#     h = [f(a+2, b, n-1), f(a, b+2, n-1), f(a*2, b, n-1), f(a, b*2, n-1)]
#     return any(h) if n % 2 != 0 else any(h)
#
# for s in range(1, 117+1):
#     if f(3, s, 2):
#         print(s)
# #15

#задание 20
# def f(a, b, n):
#     if a + b >= 122: return n % 2
#     if n < 0: return 0
#     h = [f(a+2, b, n-1), f(a, b+2, n-1), f(a*2, b, n-1), f(a, b*2, n-1)]
#     return any(h) if n % 2 != 0 else all(h)
#
# for s in range(1, 117+1):
#     if f(3, s, 3):
#         print(s)
# #9 110

# #задание 21
#
# def f(a, b, n):
#     if a + b >= 122: return n % 2
#     if n < 0: return 0
#     h = [f(a+2, b, n-1), f(a, b+2, n-1), f(a*2, b, n-1), f(a, b*2, n-1)]
#     return any(h) if n % 2 != 0 else all(h)
#
# for s in range(1, 117+1):
#     if (f(3, s, 2) or f(3,s, 4)) and not(f(3,s,2)):
#         print(s)
# #109

# #заадание 23
#
# def f(start, end):
#     if start == end: return 1
#     if start < end: return 0
#     return (f(start-1, end) + f(start//3, end))
# print(f(33, 9)*f(9,1))
#72

# #задание 24
#
# s = open('24var17-20.txt').readline()
# while 'Z' in s: s = s.replace('Z', ' ')
# res = s.split()
# print(max(len(s) for s in res))
# print(max(res, key = len))
# #34

#17 задание
# f = [int(x) for x in open('17var19.txt')]
# ans = []
#
# for i in range(len(f)-1):
#     a1 = abs(f[i])
#     a2 = abs(f[i+1])
#     if (a1 % 2 != 0) and (a1 % 10 == a2 % 10):
#         ans.append(a1 * a2)
# print(len(ans), max(ans))

#27 задачка
clastersA = [[], []]

for s in open('A27.txt'):
    s = s.replace(',', '.')
    x, y = [float(c) for c in s.split()]
    if y > 15:
        clastersA[0].append([x,y])
    else:
        clastersA[1].append([x,y])

clastersB = [[], [], []]

for s in open('B27.txt'):
    s = s.replace(',', '.')
    x,y = [float(c) for c in s.split()]
    if y > 6:
        clastersB[0].append([x,y])
    elif x > -2:
        clastersB[1].append([x,y])
    else:
        clastersB[2].append([x,y])

def dist(p1, p2):
    x1,y1,x2,y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def center(claster):
    m = []
    for p in claster:
        sm = sum(dist(p, p1) for p1 in claster)
        m.append([sm,p])
    return min(m)[1]
centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]

pxA = sum(x for x,y in centerA)/2*10000
pyA = sum(y for x,y in centerA)/2*10000
print(int(pxA), int(pyA))

pxB = sum(x for x,y in centerB)/3*10000
pyB = sum(y for x,y in centerB)/3*10000
print(int(pxB), int(pyB))

