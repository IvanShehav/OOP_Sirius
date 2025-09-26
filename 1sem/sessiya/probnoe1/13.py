def f(n):
    num = bin(n)[2:]
    res = str(sum(int(i) for i in num) % 2) + num + str(sum(int(i) for i in num) % 2)
    return int(res, 2)
list = []
for i in range(1, 100):
    if f(i) >= 43:
        list.append(f(i))
print(min(list))
