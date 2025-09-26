def f(n, stop):
    if n == stop: return 1

    if n > stop: return 0
    return (f(n+1, stop) + f(n+2, stop) + f(n+n-1, stop))
print(f(2,9))