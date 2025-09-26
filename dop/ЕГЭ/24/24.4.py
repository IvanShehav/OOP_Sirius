# f = open('z:24_2420.txt').read().strip()
# alph = 'ABEF'
# cnt = 0
# mx = 0
#
# for i in range(len(f)):
#     if f[i] in alph:
#         cnt += 1
#     else:
#         mx = max(mx, cnt)
#         cnt = 0
# print(mx)

# f = open('z:24_2426.txt').read().strip()
# alph = '123'
# cnt = 0
# mx = 0
#
# for i in range(len(f)):
#     if f[i] in alph:
#         cnt += 1
#     else:
#         mx = max(mx, cnt)
#         cnt = 0
# print(mx)

# f = open('z:24_1040.txt').read().strip()
# alph = '0123456789'
# mx = 0
# cnt = 0
#
# for i in range(len(f)):
#     if f[i] in alph:
#         cnt += 1
#     else:
#         mx = max(mx, cnt)
#         cnt = 0
# print(mx)

# f = open('z:24_1428.txt').read().strip()
# while 'XY' in f: f = f.replace('XY', 'X Y')
# while 'XZ' in f: f = f.replace('XZ', 'X Z')
# strr = f.split()
# print(len(max(strr, key=len)))


# f = open('z:24_1975.txt').read().strip()
# while 'PP' in f: f = f.replace('PP', 'P P')
# strr = f.split()
# print(len(max(strr, key=len)))


# f = open('z:24_1302.txt').read().strip()
# while 'XZZY' in f: f = f.replace('XZZY', ' ')
# strr = f.split()
# print(max(strr, key=len))


# f = open('z:24_4602.txt').read().strip()
# f = f.replace('A', 'O').replace('C', 'B').replace('D', 'B')
# f = f.replace('BO', '*').replace('O', ' ').replace('B', ' ')
# strr = f.split()
# print(len(max(strr, key=len)))

# from re import *
# f = open('z:24_4643.txt').readline()
# f = f.replace('2', '1').replace('B', 'A')
#
# reg = r'(11A)+'
#
# print(max(len(x.group())/3 for x in finditer(reg, f)))

from re import *
# f = open('z:24_8510.txt').readline()
# f = f.replace('N', 'P').replace('O', 'P')
#
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if 'PP' not in c:
#             m = max(len(c), m)
#         else:
#             break
# print(m)

# f = open('z:24_21.txt').readline()
#
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if all(c[i] != c[i+1] for i in range(len(c)-1)):
#             m = max(len(c), m)
#         else:
#             break
# print(m)

# f = open('z:24_2422.txt').readline()
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if all(c[i] <= c[i+1] for i in range(len(c)-1)):
#             m = max(len(c), m)
#         else:
#             break
# print(m)


# f = open('z:24_2423.txt').readline()
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if all(c[i] < c[i+1] for i in range(len(c)-1)):
#             m = max(m, len(c))
#         else:
#             break
# print(m)

# f = open('z:24_2427.txt').readline()
# m = 0
# ls = set()
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if all(c[i] > c[i+1] for i in range (len(c)-1)):
#             m = max(m, len(c))
#             ls.add(c)
#         else:
#             break
# print(max(ls))

# from re import *
# f = open('z:24_4113.txt').readline()
#
# reg = r'(?=((BB|DD)+))'
#
#
# print(max(len(x.group(1))/2 for x in finditer(reg, f)))

# f = open('z:24_9552.txt').readline()
#
# rr = r'(?:CSGO|PC)+'
#
# print(len(max((x.group(0) for x in finditer(rr,f)), key=len)))


# f = open("z:24_4546.txt").readline()
#
# reg = r'(A.A|C.C)+'
# rr = rf'(?=({reg}))'
#
# print(max((x.group(1) for x in finditer(rr, f)), key=len))
# print(len(max((x.group(1) for x in finditer(rr, f)), key=len))//3)


# f = open('z:24_2251.txt').readline()
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if c.count('D') <= 2:
#             m = max(m, len(c))
#         else:
#             break
# print(m)


# f = open('z:24_10105.txt').readline()
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if c.count('T') == 100:
#             m = max(len(c), m)
#         elif c.count('T') > 100:
#             break
# print(m)


# f = open('z:24_13715.txt').readline()
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if c.count('AB') == 50:
#             m = max(m, len(c))
#         elif c.count('AB') > 50:
#             break
# print(m)


# f = open('z:24_12476.txt').readline()
# m = 0
# for l in range(len(f)):
#     for r in range(l+m, len(f)):
#         c = f[l:r+1]
#         if c.count('RO') == 21 and 'ORO' not in c and 'ROR' not in c:
#             m = max(m, len(c))
#         elif c.count('RO') > 21 or 'ORO' in c or 'ROR' in c:
#             break
# print(m)


# f = open('z:24_6734.txt').readline()
# m = 10000
# for l in range(len(f)):
#     for r in range(l, l+m):
#         c = f[l:r+1]
#         if c.count('.') == 7:
#             m = min(m, len(c))
#             break
# print(m)


# f = open('z:24_11954.txt').readline()
# m = 1000000
# for l in range(len(f)):
#     for r in range(l, l+m):
#         c = f[l:r+1]
#         if c.count('X') >= 500 and 'Y' not in c:
#             m = min(m, len(c))
#         else:
#             break
# print(m)


# import re  # Необходимый импорт
#
# f = open('z:24_9169.txt').readline()
# reg = r'(?:BAD|FAT).*?(?:BAD|FAT).*?(?:BAD|FAT)'
# rr = rf'(?=({reg}))'
# matches = re.finditer(rr, f)
# print(min((x.group(1) for x in matches), key=len))

#
# f = open('z:24_5171.txt').readline()
#
# reg = r'(?=((CA)+(CA|C)))'
#
# print(max((x.group(1) for x in finditer(reg, f)), key=len))
# CACACACACACACACACACACACACACACACACACACACACACACACACACACA


