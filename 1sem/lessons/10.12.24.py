###СТЕКИ
import random


#Стек - область памяти в которой хранятся локальные переменные и адреса возврата.

#Быстрая рекурсивная сортировка
#меняем крайние элементы (которые дальше друг от друга). Нужно всего n/2 обменов
#Алгоритм

# n = 7
# a = [3,8,4,5,7,10,11]
#
def qSort(a, nStart, nEnd):
    if nStart >= nEnd: return
    L = nStart
    R = nEnd
    x = a[(L+R)//2]
    while L <= R:
        while a[L] < x: L += 1
        while a[R] > x: R -= 1
        if L <= R:
            a[L], a[R] = a[R], a[L]
            L += 1
            R -= 1
    qSort(a, nStart, R)
    qSort(a, L, nEnd)
#
#
# qSort(a, 0, len(a)-1)
# print(a)

# B = sorted(a) # алгоритм Teamsort

# #Сортировка по убыванию:
# B = sorted(a, reverse=True)
#
# #По последней цифре:
# def lastDigit(n):
#     return n % 10
# B = sorted(a, key = lastDigit)
#
# # или так:
# B = sorted(a, key = lambda x: x % 10)
#
#
# #По возрастанию без сохранения массива
# A = []
# A.sort()


a = [5, 3, 4, 2, 1, 6, 3, 2]

# half_len = len(a) // 2
#
# for i in range(half_len):
#     for j in range(half_len - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# for i in range(half_len, len(a)):
#     for j in range(half_len, len(a) - 1):
#         if a[j] < a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)

# cnt = 1
# for i in range(len(a)):
#     for j in range(len(a)-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# for i in range(len(a)-1):
#     if a[i] != a[i+1]:
#         cnt += 1
# print(a)
# print(cnt)
from random import *
def quick_sort(a):
    if len(a) <= 1:
        return a
    x = choice(a)
    b0 = [i for i in a if i < x]
    b = [i for i in a if i == 1]
    b1 = [i for i in a if i > 1]

    return quick_sort(b0) + b + quick_sort(b1)
#
# def unique_count(a):
#     count = dict()
#     for i in a:
#         if i not in count:
#             count[i] = 1
#         else:
#             count[i] += 1
#     return len(count)
#
# a = list(map(int, input().split()))
# print(quick_sort(a))
# print(unique_count(a))

##ПУЗЫРЕК
def puzirek(a):
    cnt_puz = 0
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                cnt_puz += 1
    return cnt_puz

##Сортировка выбором:
def choise_sort(a):
    cnt_choise = 0
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
        cnt_choise += 1
    return cnt_choise

#Быстрая сортировка
def quik_Sort(a, nStart, nEnd):
    cnt_quik = 0
    if nStart >= nEnd: return
    L = nStart
    R = nEnd
    x = a[(L+R)//2]
    while L <= R:
        while a[L] < x: L += 1
        while a[R] > x: R -= 1
        if L <= R:
            a[L], a[R] = a[R], a[L]
            cnt_quik += 1
            L += 1
            R -= 1
    qSort(a, nStart, R)
    qSort(a, L, nEnd)
    return cnt_quik

res_puz = 0
res_coise = 0
res_quik = 0

# for j in range(10):
#     a = [randint(-100, 100) for i in range(1000)]
#     # print(a)
#     a1 = a
#     a2 = a
#
#     res_puz += (puzirek(a))
#     res_coise += (choise_sort(a1))
#     res_quik += (quik_Sort(a2, 0, len(a2) - 1))


a = [9,7,5,3,1,2,4,6,8]
a1 = a
a2 = a

print("Пузырек: ", puzirek(a))
print('='*20)

print("Сделал выбор: ", choise_sort(a1))
print('='*20)

print("Молния Маквын: ", quik_Sort(a2, 0, len(a2) - 1))

print('='*20)


