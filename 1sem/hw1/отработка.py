# n = int(input())
#
# foods = set()
# foods2 = set()
#
# for _ in range(n):
#     eat = input()
#     foods.add(eat)
#
# for days in range(int(input())):
#     for day in range(int(input())):
#         eat = input()
#         foods2.add(eat)
#
# if (foods ^ foods2) != '':
#     print(*sorted(foods ^ foods2), sep="\n")
# else:
#     print("Готовить нечего")


# def f(n):
#     num = bin(n)[2:]
#     if n % 2 == 0:
#         num = num + '01'
#     else:
#         num = num + '10'
#     return int(num, 2)
#
# for i in range(500):
#     if f(i) > 102:
#         print(f(i))

# for A in range(32):
#     B = True
#     for x in range(32):
#         if ((x&25==0) or (x&9!=0) or (x&A!=0))==0:
#             B=False
#     if B:
#         print(A)
#         break

# def f(n):
#     if n >= 2025: return n
#     if n < 2025: return n + 3 + f(n+3)
# print(f(23) - f(21))

# def f(x, y):
#     if x == y:
#         return 1
#     if x > y:
#         return 0
#     else:
#         if x % 2 == 0:
#             return f(x + 1, y) + f(x * 1.5, y)
#         else:
#             return f(x + 1, y)
# print(f(1, 22))


def f(a, n):
    if a >= 26 or n > 2:
        return n == 2 or n == 4
    h = [f(a+1, n+1), f(a*2,n+1)]
    if n % 2 == 0:
        return all(h)
    return any(h)

for i in range(1, 26):
    if f(i, 0):
        print(i)