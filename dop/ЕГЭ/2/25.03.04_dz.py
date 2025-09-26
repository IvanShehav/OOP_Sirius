# from itertools import *
#
# def f(x, y, z):
#     return (not(x == y <= z))
#
# table = [(0,0,1), (0,1,1)]
#
# for p in permutations("xyz"):
#     if [f(**dict(zip(p, row))) for row in table] == [1, 0]:
#         print(p)

# print("x y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (not(x == (y <= z))) == 0:
#                 print(x,y,z)


from itertools import *

def f(w, x, y, z):
    return not(w) and ((y or z) <= (not(x) and y))

for a in product([0,1], repeat = 8):
    table = [(a[0], a[1], a[2], 1), (a[3], a[4], 1, a[5]), (a[6], 1, 1, a[7])]
    if len(table) == len(set(table)):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, row))) for row in table] == [1,1,1]:
                print(p)