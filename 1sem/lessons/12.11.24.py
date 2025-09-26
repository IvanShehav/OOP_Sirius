###СПИСОЧНЫЕ ВЫРАЖЕНИЯ. МОДЕЛЬ ПАМЯТИ ДЛЯ ТИПОВ ПИТОНА

# numbers = [int(input()) for i in range(5)]
# numbers = [element for element in numbers if element > sum(numbers)//len(numbers)]
#
# matrix = [[int(x) for x in input().split()] for i in range(5)]

# #проверить одинаковость значения
# x = 1
# y = 1
# print(id(x))
# print(id(y))
# print(x is y)

# a,b = map(int, input().split())
# print([i**2 for i in range(a, b+1)])

# n = input().split()
# print([len(n[i]) for i in range(len(n))])

# b = input()
# print([len(i) for i in b.split()])

# num = [int(i) for i in input().split()]
# print({i for i in num if i % 2 != 0})

# num = [int(i) for i in input().split()]
# print({i for i in num if i**0.5 == int(i**0.5)})

# word = input()
# print({i:word.lower().count(i) for i in word.lower() if i.isalpha()})
#
# numbers = {int(i) for i in input().split()}
# print({n: [i for i in range(1, n+1) if n%i == 0] for n in numbers})

# print(''.join(i[0].upper() for i in input().split()))

# n = map(int, input().split())
# # print(*sorted([i for i in set(n)]), sep=' - ')
# print([' - '.join(str(i)) for i in sorted(set(n))])

# rle = [('a', 2), ('b', 5), ('c', 4)]
# print(''.join([i*j for i, j in rle]))




###ЗАДАЧИ

# string = input().split()
# for i in range(0, len(string)):
#     print(i+1, '. ', string[i], sep='')


from itertools import *

# n = int(input())
# list1 = []
# for _ in range(n):
#     list1.append(input())
#
# res = list(combinations(list1, 2))
#
# for i in range(len(res)):
#     print(f'{res[i][0]} - {res[i][1]}')

##TASK_2
# word = input()
# a = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
# b = ["пик", "треф", "бубен", "червей"]
# b.remove(word)
# val = list(product(a, b))
#
# for i in val:
#     print(i[0], i[1])

##TASK_3

lst = ''
for _ in range(int(input())):
    lst = lst + input() + ' '
day = int(input())
lst.split()
print(lst)

print(list(islice(lst,0 , day-1)))

## ввод массив, фор ин и слайс и вывод


