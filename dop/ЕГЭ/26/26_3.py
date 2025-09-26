l = open("26_3.txt")
n = int(l.readline())
dict = [0] * 86400
for x in [i for i in l]:
    i, j = map(int, x.split())
    for m in range(i, j):
        dict[m] += 1
k = max(dict[54000 - 1:75600])
print(k)
print(len([i for i in dict[54000 - 1:75600] if i == k]))