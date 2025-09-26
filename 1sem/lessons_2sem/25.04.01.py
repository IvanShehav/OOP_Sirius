# k = 0
# for s in open('z:9_2103.txt'):
#     a,b,c,d = map(int, s.split())
#     k += a == c and b == d and a != b
# print(k)

# k = 0
# for s in open('z:9_2095.txt'):
#     a, b, c = map(int, s.split())
#     k += (a == b and b != c) or (a == c and c != b) or (b == c and c != a)
# print(k)

# k = 0
# for s in open('z:9_2034.txt'):
#     a, b, c = map(int, s.split())
#     k += a + b + c == 180
# print(k)

# k = 0
# p = 0
# for s in open('z:9_2099.txt'):
#     a, b, c = map(int, s.split())
#     k += a + b + c == 180
#     p += (a + b + c == 180) and ((a == b == c) or (a == b or b == c or a == c))
# print(p/k * 100)


# k = 0
# for s in open('z:9_2047.txt'):
#     a, b, c, d = map(int, s.split())
#     # p += (a + b + c + d == 360) and ((a == d and b == c and a != b) or (a == c and b == d and a != b) or (a == b and c == d) and a != c)
#     k += (a == c and b == d) and (a + b + c + d == 360)
# print(k, p)

# k = 0
# for s in open('z:9_2041.txt'):
#     *a, b = sorted(map(int, s.split()))
#     k += sum(a) > b
# print(k)


# k = 0
# for s in open('z:9_2043.txt'):
#     c,d,e,f = map(int, s.split())
#     k += (c == e and d == f)
# print(k)

# ans = []
# for s in open("z:9_2100.txt"):
#     a, b, c = sorted(map(int, s.split()))
#     if a**2 + b**2 == c**2:
#         ans.append(a+b)
# print(max(ans))
#
# k = 0
# for s in open('z:9_2101.txt'):
#     a, b, c = sorted(map(int, s.split()))
#     k += (a+b>c) and (a**2 + b**2 > c**2)
# print(k)

k = 0
for s in open('z:9_2096.txt'):
    x1,y1,x2,y2 = map(int,s.split())
    if (x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0) or (x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0) or (x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0) or (x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0):
        k += 1
print(k)
