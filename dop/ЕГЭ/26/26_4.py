f = open('26_4.txt')
n = int(f.readline())
a = sorted([int(f.readline()) for i in range(n)], reverse=True)

cnt = 1
first = a[0]

for i in range(1, len(a)):
    if (first - a[i]) >= 4:
        first = a[i]
        last = a[i]
        cnt += 1

print(cnt, a[i])