#найти все простые числа в диапазоне от 2 до 1000:

def isPrime(n):
    k = 2
    while k*k <= n and n % k != 0:
        k += 1
    return (k*k > n)