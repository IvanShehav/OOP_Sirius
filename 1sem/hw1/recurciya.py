# import sys
# sys.setrecursionlimit(10**6)
# def funct(n):
#     if n < 3:
#         return n
#     elif n >= 3:
#         return ((n-1) * funct(n-2))
#
# print((funct(2025)-funct(2023))//funct(2021))



# def F(n):
#     if n == 0:
#         return 0
#     elif n % 2 == 1:
#         return F(n-1) + 2*n - 1
#     elif n % 2 == 0:
#         return 4*F(n/2)
#
# maxi = 0
#
# for b in range(0,1045):
#     for a in range(0,1045):
#         if F(a) - F(b) == 1045:
#             maxi = max(maxi, a - b)
# print(maxi)


# def F(n):
#     if n == 0:
#         return 1
#     elif n % 2 == 1:
#         return ((n%10)*F(n//100))
#     elif n % 2 == 0 and n > 0:
#         return F(n//100)
# cnt = 0
# for k in range(10**7, 9*10**7+1):
#     if F(k) == 25:
#         cnt += 1
# print(cnt)


# def F(n):
#     if n >= 2000:
#         return 2000
#     elif n % 2 == 1 and n < 2000:
#         return n * F(n+1)
#     elif n % 2 == 0 and n < 2000:
#         return n * (F(n+1)/2)
#
# print (int(F(1998)/F(2001)))

import sys
sys.setrecursionlimit(10**9)

# a_3 = len(range(123456798, 1234567886, 3))
# a_5 = len(range(123456800, 1234567886, 5))
# a_15 = len(range(123456810, 1234567886, 15))
# print(len(range(123456798, 1234567886)) - a_3 - a_5 + a_15)


# def f(n):
#     if n == 0:
#         return 0
#     elif n > 0 and n % 2 == 0:
#         return f(n/2)
#     elif n % 2 == 1:
#         return 1 + f(n-1)
#
# for i in range(10000):
#     if f(i) == 11:
#         print(i)
#         break


# def f(n):
#     if n == 0:
#         return 0
#     elif n > 0 and n % 3 == 0:
#         return n + f(n-3)
#     elif (n % 3) > 0:
#         return n + f(n-(n%3))
#
# print(f(26))


# def f(n):
#     if n == 1:
#         return 1
#     elif n % 2 == 0:
#         return n + f(n-1)
#     elif n % 2 == 1 and n > 1:
#         return 2*f(n-2)
# print(f(26))

# def f(x, y):
#     if x < y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x-2,y) + f(x-3,y) + f(x//3,y)
# print(f(20,3))

# def f(x,y):
#     if x > y or x == 15:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+1, y) + f(x+3, y) + f(x * 3, y)
# print (f(7,14) * f(14,20))


# def f(x,y):
#     if x > y or x == 26:
#         return 0
#     if x == y:
#         return 1
#     return f(x+1,y) + f(2*x + 1,y)
# print(f(1,27))

# def f(x,y,k):
#     if x > y + 1:
#         return 0
#     if x == y:
#         return 1
#     if k == 1:
#         return f(x + 3, y, k - 1) + f(x * 2, y, k-1)
#     else:
#         return f(x-1,y, k+1) + f(x+3, y, k) + f(x*2, y, k)
# print(f(4,14,0))


# def f(start, end):
#     if start > end or start == 5 or start == 10:
#         return 0
#     if start == end:
#         return 1
#     return f(start+1, end) + f(start*2, end) + f(start+3,end)
# print(f(2,14))


# def f (x, end):
#     if x < end:
#         return 0
#     if x == end:
#         return 1
#     return f(x-2, end) + f(x//2, end)
# print(f(38,16)*f(16,2))

# def f(x,end):
#     if x > end:
#         return 0
#     if x == end:
#         return 1
#     return f(x+1, end) + f(x+2, end) + f(x+3, end)
# print(f(1,7)*f(7,35))


name = input()
num = int(input())
print(f"Группа №{num // 100}.")
print(f"{num % 10}. {name}.")
print(f"Шкафчик: {num}.")
print(f"Кроватка: {(num // 10) % 10}.")