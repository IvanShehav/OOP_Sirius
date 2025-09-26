def divs(x):
    k = 2
    d = set()
    while k**2 <= x:
        if x % k == 0:
            d.add(k)
            d.add(x//k)
        k +=1
    return sorted(d)

def s(x):
    d = [i for i in divs(x) if i <= x // 2]
    if len(d) < 3:
        return False
    return sum (d[-3:])


a = 1200000
k = 0

while k < 5:
    b = s(a)
    if b > 0 and b % 2022 == 0 and b != a:
        k += 1
        print(a, b)
    a -= 1