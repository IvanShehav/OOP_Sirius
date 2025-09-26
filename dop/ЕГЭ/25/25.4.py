def divs(x):
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            return d, x//d
    return 0, 1

c = 0
for i in range(800001, 10**100):
    ds = divs(i)
    if sum(ds) % 138 == 0:
        print(i, sum(ds))
        c += 1
        if c == 5:
            break