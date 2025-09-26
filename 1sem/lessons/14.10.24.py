import random
from random import randint

# A = [randint(-100,100) for x in range(5)]
# print(*A)
# print(f'Максимальный элемент A [{A.index(max(A))}]: {max(A)}')
# print(f'Минимальный элемент A [{A.index(min(A))}]: {min(A)}')

##реверс массива
#for i in range(N//2):
#   A[i], A[N-1-i] = A[N-1-i], A[i]
# или можно использовать спец функцию
# A.reverse()

##сдвиг массива на 1 элемент
# c = A[0]
# for i in range(N-1):
#     A[i] = A[i+1]
# A[N-1] = c

##срезы в массивах
# A[1:6:2] - с 1 эл по 6 с шагом 2

##отбор по условию в питоне
# B = [ x for x in A if x % 2 == 0]

# A=[1,2,3]
# B = A.copy()
#
# print(B)

##задача 1
# A = [randint(-10, 10) for x in range(7)]
# B = []
#
# for num in A:
#     if num % 2 == 0:
#         B.append(num)
# print("Массив А:", *A)
# print("Массив B:", *B)

##задача 1
# A = [randint(0, 100) for x in range(5)]
# print("Массив:", *A)
# num = A[0]
# count = len(A)
# for i in range(len(A)-1):
#     A[i] = A[i+1]
# A[count-1] = num
# print("Результат:", *A)

##задание 2
# A = [randint(0, 100) for x in range(6)]
# print(*A)
# mas1 = A[:len(A)//2]
# mas2 = A[len(A)//2:]
# mas1.reverse()
# mas2.reverse()
# print("Результат:", *mas1, *mas2)

# ##задание 3
# a = [randint(-100, 100) for x in range(6)]
# print("Массив", *a)
# b = []
# c = []
# for i in range(len(a)):
#     if a[i] <= 0:
#         c.append(a[i])
#     else:
#         b.append(a[i])
# d = []
# d.extend(b)
# d.extend(c)
# print("Результат:", *d)
# print(f'Положительные: ', *b)

##задача 2
# a = [randint(0, 100) for x in range(5)]
# res = []
#
# for i in range(len(a)):
#     c = 0
#     if c == 0:
#         while a[i] > 0:
#             for j in range(2, a[i]-1):
#                 if a[i] % j == 0:
#                     c += 1

##задача 3
def fib(x):
    a, b = 5 * (x**2) + 4, 5 * (x**2) - 4
    if int(a) == a or int(b) == b:
        return True
    return False
num = [randint(0, 100) for x in range(5)]
print(*num)
res = [i for i in num if fib(i)]
print(res)
