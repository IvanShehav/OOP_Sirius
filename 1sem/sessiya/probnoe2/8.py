def f(s,n):
    if s >= 112: return n % 2 == 0
    if n < 0: return 0
    h = []
    if (s + 1) % 2 == 0:
        h.append(f(s + 1, n - 1))
    if (s + 2) % 2 == 0:
        h.append(f(s + 2, n - 1))
    if (s * 2) % 2 == 0:
        h.append(f(s * 2, n - 1))
    return any(h) if n % 2 != 0 else all(h)
for s in range(1, 111+1):
    if f(s,4):
        print(s)