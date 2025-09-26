f = open('24.txt')
s = f.readline()
mc = 0
for i in range (len(s)-1):
    cf, cl = 0, 0
    count = 0
    for j in range(i, len(s)):
        count += 1
        if s[j] == 'C':
            cf += 1
        elif s[j] == 'D':
            cl += 1
        if cf > 3 or cl > 3:
            mc = max(mc, count - 1)
            break
print(mc)