# def f(s, n):
#     if s >= 112 or n > 4:
#         return n == 4
#     h = []
#     if (s+1) % 2 == 0:
#         h.append(f(s+1, n+1))
#     if (s+2) % 2 == 0:
#         h.append(f(s+2, n+1))
#     if (s*2) % 2 == 0:
#         h.append(f(s*2, n+1))
#     if n % 2 == 0:
#         return all(h)
#     else:
#         return any(h)
#
# for s in range(1,111+1):
#     if f(s, 0):
#         print(s)

def f(s,n):
    if s >= 112: return n % 2 == 0
    if n < 0: return 0
    h = []
    if (s+1) % 2 == 0:
        h.append(f(s+1, n-1))
    if (s+2) % 2 == 0:
        h.append(f(s+2, n-1))
    if (s*2) % 2 == 0:
        h.append(f(s*2, n-1))
    return any(h) if n % 2 != 0 else all(h)

for s in range(1, 112):
    if f(s, 4) and not(f(s,2)):
        print(s)

