n = 1

def gcd (a, b):
    while b != 0:
        a, b = b, a % b
    return(a)

for x in range(10**9+1, 10**20):
    if n > 5:
        exit()
    if str(x) == (str(x)[::-1]):
        if gcd(int(x), int(str(x)[::-1])) % 7 == 0:
            print(x)
            n += 1