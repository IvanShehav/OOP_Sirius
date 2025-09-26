#множества словари

# word = input()
# word2 = input()
# print(*(set(word) & set(word2)), sep = "")

# items = set()
#
# for _ in range(int(input())):
#     string = input()
#     items |= set(string.split())
#
# for item in items:
#     print(item)


# n, m = int(input()), int(input())
#
# items_n = set()
# items_m = set()
#
# for _ in range(n):
#     items_n.add(input())
#
# for _ in range(m):
#     items_m.add(input())
#
# count = items_m & items_n
#
# if len(count) > 0:
#     print(len(count))
# else:
#     print("Таких нет")

# n, m = int(input()), int(input())
#
# items_n = set()
# items_m = set()
#
# for _ in range(n):
#     items_n.add(input())
#
# for _ in range(m):
#     items_m.add(input())
#
# count = items_m ^ items_n
#
# if len(count) > 0:
#     print(len(count))
# else:
#     print("Таких нет")

uravnenie = input()
numbers = input().split(',')

for i in numbers:
    res = eval(uravnenie.replace('x', numbers[i]))
    print(res)






