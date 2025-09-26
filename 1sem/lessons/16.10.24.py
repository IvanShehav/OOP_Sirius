from random import *

### СОРТИРОВКА МАССИВОВ

### ВИДЫ СОРТИРОВОК:

# #1. Метод пузырька
# A = [24, 3421, 124, 16, 8367, 10, 9, 2]
# N = len(A)
# for i in range(N-1):
#     for j in range(N-2, i-1, -1):
#         if A[j+1] < A[j]:
#             A[j], A[j+1] = A[j+1], A[j]

## 2) Метод камня - обратная сортировка методу пузырька

# ## 3) Метод выбора (минимального элемента)
# for i in range(N-1):
#     nMin = i
#     for j in range(i+1, N):
#         if A[j] < A[nMin]:
#             nMin = j
#     if i != nMin:
#         A[i], A[nMin] = A[nMin], A[i]

# чтобы сортировать по возрастанию можно использовать команду "sorted()"
# B = sorted(A)

# сортировка по убыванию:
# B = sorted(A, reverse = True)

# есть еще a.sort()


##Задачи

# ##метод камушков
# a = [randint(-100, 100) for i in range(10)]
#
# for i in range(len(a)):
#     for j in range(0, len(a)-1):
#         if a[j + 1] > a[j]:
#             a[j], a[j+1] = a[j+1], a[j]
#
# print(*a)


# #задача 2
# a = [randint(-100, 100) for i in range(10)]
#
# wasIt = False
# for i in range(len(a)-1):
#     for j in range(len(a)-2, i-1, -1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#             wasIt = True
#     if not wasIt:
#         break
# print(*a)

# ## задача 3
# def f(n):
#     s=0
#     n = abs(n)
#     while n != 0:
#         s=s+(n%10)
#         s //= 10
#     return s
#
# a = [randint(-100, 100) for i in range(3)]
#
# for i in range(len(a)-1):
#     for j in range(len(a)-2, i-1, -1):
#         if f(a[j]) > f(a[j+1]):
#             a[j], a[j+1] = a[j+1], a[j]
# print(*a)

##задача 4
def sortt(mass):
    for n in range(len(mass)//2-1):
        temp = n
        for mak in range(n+1, len(mass)):
            if mass[mak] < mass[temp]:
                temp = mak
        if n != temp:
            mass[n], mass[temp] = mass[temp], mass[n]

    for n in range(len(mass)//2, len(mass)+1):
        temp = n
        for mak in range(n+1, len(mass)):
            if mass[mak] < mass[temp]:
                temp = mak
        if n != temp:
            mass[n], mass[temp] = mass[temp], mass[n]

    return mass

a = [randint(-100, 100) for x in range(5)]

mas1 = [a[i] for i in range(len(a//2))]
mas2 = [a[i] for i in range(len(a//2))]

print(sortt(a))
