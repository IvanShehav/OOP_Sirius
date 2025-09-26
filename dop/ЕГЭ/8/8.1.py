from itertools import *

count = 0

for i in product('0123456789ABCDEF', repeat=5):
    if i.count('6') == 2:
        id = i.index('6')
        if (i[id-1] and i[id+1]) != '02468ACE':
            if i[0] != '0':
                count+=1
print(count)