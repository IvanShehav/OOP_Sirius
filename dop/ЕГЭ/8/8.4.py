from itertools import *

cnt = 0
for i in permutations('0123456789', 7):
    a = ''.join(i)
    if a[0] != '0':
        q = a
        for j in range(7):
            if j % 2 == 0:
                q = q.replace(str(j), 'x')
            else:
                q = q.replace(str(j), 'y')
        if 'xx' not in q and 'yy' not in q:
            cnt+=1

print(cnt)