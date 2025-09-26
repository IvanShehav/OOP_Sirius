# s = open('24_demo.txt').readline()
#
# cnt = 0
# mx = 0
#
# for i in range(len(s)-1):
#     if s[i] == 'Y' and s[i+1] == 'Y':
#         cnt += 1
#     else:
#         mx = max(cnt, mx)
#         cnt = 1
# print(mx)

# s = open('24.txt').readline()
# cnt = 0
# mx = 0
#
# for i in range(len(s)-2):
#     s1 = s[i] + s[i+1] + s[i+2]
#     cnt += 1
#     mx = max(mx, cnt)
#     if s1.count('X') == 1 and s1.count('Y') == 1 and s1.count('Z') == 1:
#         cnt = 0
# print(mx - 3)

# f = open('24 (1).txt').readline()
# mx = 0
# cnt = 0
# s = []
#
# for i in range(len(f)):
#     if f[i:i+2] == 'WW':
#         s.append(i)
# for x in range(101, len(s)):
#     cnt = s[x] - s[x-101]
#     mx = max(mx, cnt)
# print(mx)
#


f = open('24 (2).txt').readline()
cnt = 0
mx = 0
for i in range(len(f)-1):
    strr = f[i] + f[i+1]
    if 'ad' not in strr and 'da' not in strr:
        cnt += 1
    else:
        mx = max(mx, cnt)
        cnt = 0
print(mx+1)








