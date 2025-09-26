import sys
sys.setrecursionlimit(5000)

def f(n):
    if n > 1_000_000: return n
    if n <= 1_000_000: return n + f(n*2)

def g(n):
    return f(n)/n

cnt = 0
for i in range(1, 100000):
    if g(i) == g(2000):
        cnt += 1
print(cnt)