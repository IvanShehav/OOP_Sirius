def f(n, end):
    if n == end: return 1
    if n > end: return 0
    return f(n+1, end) + f(n+2, end) + f(n + n - 1, end)

print(f(2,9))
