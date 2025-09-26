menu = []
m = int(input())
for _ in range(m):
    menu.append(input())
n = int(input())
flag = 1
if n <= m:
    for i in range(n):
        print(menu[i])
else:
    for i in range(n//m):
        for j in range(m):
            print(menu[j])
    for j in range(n%m):
        print(menu[j])

