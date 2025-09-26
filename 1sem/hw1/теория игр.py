# def f(a, b, n):
#     if a + b >= 93 or n > 2:
#         return n == 2
#     h = [f(a+1, b, n+1), f(a*2,b,n+1), f(a, b+1, n+1), f(a,b*2,n+1)]
#     if n % 2 == 0:
#         return all(h)
#     return any(h)
#
# for s in range(1, 80+1):
#     if f(12, s, 0):
#         print(s)



# def f(a,b,n):
#     if a + b >= 59 or n > 4:
#         return n == 2 or n == 4
#     h = [f(a+1, b, n+1), f(a*2,b,n+1), f(a, b+1, n+1), f(a,b*2,n+1)]
#     if n % 2 == 0:
#         return all(h)
#     return any(h)
#
# for s in range(1,53+1):
#     if f(5, s, 0):
#         print(s)



def f(a,b,n):
    if a+b >= 61 or n > 2:
        return n == 2 or n == 4
    if a < b:
        h = [f(a+2,b,n+1), f(a*2,b,n+1), f(a+1, b, n+1)]
    else:
        h = [f(a, b + 2, n + 1), f(a, b * 2, n + 1), f(a, b + 1, n + 1)]

    if n % 2 == 0:
        return all(h)
    return any(h)

for s in range(1,52+1):
    if f(8, s, 0):
        print(s)