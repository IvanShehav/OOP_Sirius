# from re import *
# s = open('z:24_4627.txt').read()
#
# ch = r'(?:NPO|PNO)+'
# matches = findall(ch, s)
#
# print(len(max(matches, key =len))/3)

# #26 задачи
# n, *a = map(int,open('z:26_21424.txt'))
# a.sort(reverse=1)
# k = 1
# y = a[0]
#
# for x in a:
#     if y >=x+9:
#         k += 1
#         y = x
# print(k,y)

(n,), *a = (tuple(map(int, s.split())) for s in open('z:26_19256.txt'))

a.sort()

d = {}
for i, j in a:
    if i in d:
        d[i].append(j)
    else:
        d[i] = [j]
m = 0
for i, z in d.items():
    z.sort()
    k = 0
    for x,y in zip(z, z[1:]):
        if y - x == 1:
            k += 1
            if k > m:
                m, ID = k, i
            elif k == m:
                ID = min(i, ID)
            else:
                k = 0
print(ID, m+1)
