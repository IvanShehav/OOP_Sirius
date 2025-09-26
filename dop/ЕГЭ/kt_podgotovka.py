# # -3 //2(округление в большую)
# # побдеа при <= 72
# # 50, s - начало
#
# def f(a,b,n):
#     if a + b <= 72 or n > 2:
#         return n == 2 or n == 4
#     h = [f(a-3, b, n+1), f((a+1)//2, b, n+1), f(a, b-3, n+1), f(a, (b+1)//2, n+1)]
#     if n % 2 == 0:
#         return all(h)
#     else:
#         return any(h)
#
# for s in range(22, 500):
#     if f(50, s, 0):
#         print(s)


# ## 2 задание
# #
# def f(n):
#     num = bin(n)[2:]
#     if n % 5 == 0:
#         num = num[:3] + num
#     else:
#         num = num + bin((n%5)*5)[2:]
#     return int(num,2)
# #
# for i in range(999, 0, -2):
#         if f(i) < 313:
#             print(i)
#             break



#алгоритм евклида
# while b != 0:
#         a, b = b, a % b
#     return a
# 3 задагие
# def gcd(*numbers):
#     num = [i for i in numbers]
#     for i in range(len(num)-1):
#         while num[i+1] != 0:
#             num[i], num[i+1] = num[i+1], num[i] % num[i+1]
#         return num[i]
#
# print(gcd(36, 48, 156))

#4 задание

# from sys import setrecursionlimit
# setrecursionlimit(5000)
# def f(x,y,d):
#   if x > y or x == 30:
#     return 0
#   if x == y:
#     return 1
#   else:
#     return f(x+d,y,d) + f(x*2,y,d)
#
# k = 0
# for d in range(1,1000):
#     if f(1,10, d)*f(10,100,d):
#         k+=1
# print(k)


#5 задание

# for a in range(1, 1000):
#     flag = True
#     for x in range(0, 1000):
#         if ((x & 57 == 0) or ((x & 23 == 0) <= (not(x & a == 0)))) == False:
#             flag = False
#             break
#     if flag == True:
#         print(a)


#задание 6
# def convert_to_base(n, base):
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if n < base:
#         return digits[n]
#     return convert_to_base(n // base, base) + digits[n % base]
#
# input_number = 16847
# base = 18
# result = convert_to_base(input_number, base)
# print(result)

# #задание 7
# from functools import *
# @lru_cache(None)
# def f(n):
#     if n == 1: return 0
#     if n == 2: return 1
#     if n == 3: return 1
#     if n > 3:
#         return f(n-3) + f(n-2) + f(n-1)
# print(f(58))

#задание 8
# from random import *
# def merge(cort1, cort2):
#     num1 = [s for s in cort1]
#     num2 = [s for s in cort2]
#     res = num1 + num2
#
#     #соритровка
#     def quiksort(res):
#         if len(res) <= 1:
#             return res
#         else:
#             elem = choice(res)
#             l_m = []
#             m_m = []
#             r_m = []
#             for i in res:
#                 if i < elem:
#                     l_m.append(i)
#                 elif i > elem:
#                     r_m.append(i)
#                 else:
#                     m_m.append(i)
#             return quiksort(l_m) + m_m + quiksort(r_m)
#      #перевод обатно в кортеж
#     return tuple(quiksort(res))
#
# print(merge((1,2,5,6,9,125), (4,7,23,465,2525)))


##теория игр
# def f(a,b,n):
#     if a + b >= 59 or n > 2:
#         return n == 2 or n == 4
#     h = [f(a+2, b, n+1), f(a*2, b, n+1), f(a, b+2, n+1), f(a,b*2,n+1)]
#     if n % 2 == 0:
#         return all(h)
#     return any(h)
#
# for s in range(1,53+1):
#     if f(5,s,0):
#         print(s)

# def to_string(*elem, sep = ' ', end = '\n'):
#     return sep.join(str(item) for item in elem) + end


# def merge(horse, chees):
#     horse = list(horse)
#     chees = list(chees)
#     a = abs(horse[0] - chees[0])
#     b = abs(horse[1] - chees[1])
#     return ((a == 1 and b == 2) or (a==2 and b ==1))

# def f(n):
#     if n == 0: return 0
#     if n > 0 and n % 2 == 0:
#         return f(n/2)
#     if n % 2 != 0:
#         return 1 + f(n-1)
# cnt = 0
#
# for n in range (1, 1001):
#     if f(n) == 3:
#         cnt += 1
# print(cnt)


# def f(start, end):
#     if start == end: return 1
#     if start > end: return 0
#     return (f(start+3, end) + f(start+5,end) + f(start*2, end))
# a = f(10,20) * f(20,40)
# b = f(10,30) * f(30, 40)
# c = f(10, 20) * f(20,30) * f(30, 40)
# print(a + b - c)


# def f(n):
#     num = ''
#     dupl_n = n
#     while n > 0:
#         num = str(n % 4) + num
#         n //= 4
#
#     if int(num) % 3 == 0:
#         res = num[-1] + num[1:-1] + num[0] + '1'
#     else:
#         res = num + str(int(num) % 3)
#     return int(res,4)
# mx = 0
# for s in range(1, 100):
#     if f(s) <= 340:
#         if f(s) > mx:
#             mx = f(s)
# print(mx)



# def f(a, n):
#     if a >= 129 or n > 2:
#         return n == 2 or n == 4
#     h = [f(a+1, n+1), f(a*2, n+1)]
#
#     if n % 2 == 0:
#         return all(h)
#     return any(h)
#
# for s in range(1, 128+1):
#     if f(s, 0):
#         print(s)
