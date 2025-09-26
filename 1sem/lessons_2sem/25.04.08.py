#алгоритм поиск делителей

def divs(n):
    L = [1]
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            L += [d]
            if d*d !=n:
                L += [n//d]
    return sorted(L+[n])
print(*divs(42))


def fcrt(n):
    d = 2; L = []
    while d <= n:
        if n % d == 0:
            n //= d
            L += [d]
        else:
            d += 1
    return L

#количесвто всех делителей
# x = a**i + b **j + c**k
# количесвто делителей = (1+i)*(j+1)*(k+1)


def cnt_divs(n):
    d = 2; k = 1
    while d <= n:
        if n % d == 0:
            m = 0
            while n%3 == 0: m+= 1; n//=d
            k *= m+1
        d += 1
    return k

