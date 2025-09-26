lst = []
m = int(input())
for i in range(m):
    lst.append(input())
n = int(input())
res = []
if n <= m:
    for i in range(n):
        res.append(lst[i])
elif n > m:
    for i in range(n//m):
        for j in range(m):
            res.append(lst[j])
    for i in range(n % m):
        res.append(lst[i])

for i in range(len(res)):
    print(res[i])