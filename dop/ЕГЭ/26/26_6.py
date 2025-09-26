# f = open('z:24.txt').read()
# while 'AB' in f: f = f.replace('AB', '+')
# while 'CB' in f: f = f.replace('CB', '+')
# cnt = 0
# mx = 0
#
# for i in range(len(f) - 1):
#     if f[i] == '+' and f[i+1] == '+': ##+1
#         cnt += 1
#     else:
#         mx = max(mx, cnt)
#         cnt = 0
# print(mx+1)
#


# f = open('z:24 (1).txt').read()
# lst = []
#
# for i in range(len(f)-4):
#     first = f[i:i+2]
#     second = f[i+3:i+5]
#     if first == second[::-1]:
#         lst.append(f[i:i+5])
#     else:
#         continue
# print(len(lst))


f = open('z:24 (2).txt').read()
key = 0
mn = []
for i in range(len(f)):
        if f[i] == 'E':
            key = 1
            for j in range(i+1, len(f)):
                if f[j] == 'E':
                    key += 1
                if key == 100:
                    mn.append(j-i+1)
                    break
print(min(mn))
