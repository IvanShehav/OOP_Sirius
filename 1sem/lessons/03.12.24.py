# ### ТЕОРИЯ ИГР
#
# def f(x,h):
#     if x >= 151 and h == 3:
#         return True
#
#     if x < 151 and h == 3:
#         return False
#
#     if x % 3 == 0:
#         return False
#     return f(x+1, h+1) or f(x+2,h+1) or f(x*2, h+1)
#
# for s in range(1, 150):
#     if f(s, 1) == True:
#         print(s)


## >= 47 (10, S) +1 и +2 или *2

# def f(x,y,h):
#     if x+y >= 47 and (h == 3 or h == 5):
#         return True
#     else:
#         if x+y < 47 and h == 5:
#             return False
#         else:
#             if x+y >= 47:
#                 return False
#     if h % 2 == 0:
#         return f(x + 1, y + 2, h + 1) or f(x + 2, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
#     else:
#         return f(x + 1, y + 2, h + 1) and f(x + 2, y + 1, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)
#
# def f2(x,y,h):
#     if x+y >= 47 and h == 3:
#         return True
#     else:
#         if x+y < 47 and h == 3:
#             return False
#         else:
#             if x+y >= 47:
#                 return False
#     if h % 2 == 0:
#         return f2(x + 1, y + 2, h + 1) or f2(x + 2, y + 1, h + 1) or f2(x * 2, y, h + 1) or f2(x, y * 2, h + 1)
#     else:
#         return f2(x + 1, y + 2, h + 1) and f2(x + 2, y + 1, h + 1) and f2(x * 2, y, h + 1) and f2(x, y * 2, h + 1)
#
#
# for i in range(1, 37):
#     if f(10, i, 1):
#         print(i)
# print("===============")
# for i in range(1, 37):
#     if f2(10, i, 1):
#         print(i)


## +1 +4 *3
## >=41
## Ваня первым после неудач Пети

# def f(x,h):
#     if x >= 41 and (h == 3):
#         return True
#     else:
#         if x < 41 and h == 3:
#             return False
#         else:
#             if x >= 41 and h != 3:
#                 return False
#     if h % 2 == 0:
#         return f(x+1, h+1) or f(x+4, h+1) or f(x*3, h+1)
#     else:
#         return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 3, h + 1)
#
# for i in range(1, 41):
#     if f(i,1) == True:
#         print(i)


## +1 +2 *2
## >=103

def f(a, n):
    if a >= 103 or n > 2:
        return n == 2
    t = []

    if (a + 1) % 3 != 0:
        t.append(f(a + 1, n + 1))
    if (a + 2) % 3 != 0:
        t.append(f(a + 2, n + 1))
    if (a * 2) % 3 != 0:
        t.append(f(a * 2, n + 1))

    if n % 2 == 0:
        return all(t)
    return any(t)


print([s for s in range(1, 103) if f(s, 0)])
