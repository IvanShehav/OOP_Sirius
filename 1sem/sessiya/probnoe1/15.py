from itertools import *
cnt = 0
list = []
for i in product('ЕКМОПРТЬ', repeat=5):
    line = ''.join(i)
    cnt += 1
    if 'К' not in line and line.count('Р') == 2:
        list.append(cnt)
print(list[-1])
