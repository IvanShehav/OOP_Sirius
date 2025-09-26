a = [int(x) for x in open('../../dop/ЕГЭ/17/17.txt')]
mx = 0

res = []

for i in range(len(a)):
    if (a[i] % 100) == 13 and a[i] >= mx:
        mx = a[i]


for i in range(len(a)-2):
    c = 0
    if len(str(a[i])) == 3:
        c += 1
    if len(str(a[i+1])) == 3:
        c += 1
    if len(str(a[i+2])) == 3:
        c += 1

    if c == 2:
        if (a[i]+a[i+1]+a[i+2]) <= mx:
            res.append(a[i]+a[i+1]+a[i+2])
print(len(res), max(res))