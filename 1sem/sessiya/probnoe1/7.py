from sys import *
setrecursionlimit(10**9)
def f(n):
    if n > 1000000: return n
    if n <= 1000000: return n + f(2*n)
def g(n):
    return f(n)/n
cnt = 0
znach = g(2000)
for n in range(1, 10000):
    if g(n) == znach:
        cnt += 1
print(cnt)