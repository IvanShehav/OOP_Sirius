from itertools import *

cnt = 0
res = set()

# for i in product('0123456789AB', repeat=5):
#     a = ''.join(i)
#     s = a.count('9') + a.count('A') + a.count('B')
#     if a.count('7') == 1 and s <= 3 and a[0] != '0':
#         res.add(a)
# print(len(res))

# for i in product('012345', repeat=7):
#     a = ''.join(i)
#     if a.count('2') == 1 and a[0] != '0':
#         q = a.replace('0', 'x')
#         q = q.replace('4', 'x')
#         if '2x' not in q and 'x2' not in q:
#             res.add(a)
# print(len(res))

# alph = '0123456789ABC'
#
# nechet = '13579B'
#
# for i in product(alph, repeat=6):
#     a = ''.join(i)
#     if a.count('5') <= 1 and a[0] != '0':
#         valid = True
#         for j in range(5):
#             if a[j] in nechet and a[j+1] in nechet:
#                 valid = False
#                 break
#         if valid:
#             cnt += 1
#
# print(cnt)

# alph = '0123456789AB'
#
# for i in product(alph, repeat=7):
#     a = ''.join(i)
#     if a[0] != '0':
#         valid = False
#         for j in range(6):
#             if int(a[j], 12) % 3 == 0 and int(a[j+1], 12) % 3 != 0:
#                 valid = True
#             elif int(a[j], 12) % 3 != 0 and int(a[j+1], 12) % 3 == 0:
#                 valid = True
#             else:
#                 valid = False
#                 break
#         if valid:
#             cnt += 1
#
# print(cnt)

chet = {'0', '2', '4', '8', 'A', 'C', 'E'}

for i in product('0123456789ABCDEF', repeat=5):
    a = ''.join(i)
    if a.count('6') == 2:
        valid = True
        for j in range(4):
            if a[j] == '6' and a[j + 1] in chet:
                valid = False
                break
            if a[j + 1] == '6' and a[j] in chet:
                valid = False
                break
        if valid:
            cnt += 1
print(cnt)


