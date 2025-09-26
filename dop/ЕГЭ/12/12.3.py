mx = 0
n_min = 10000
for n in range(4,1000):
    str = '4' * 20 + '5'*n + '7'*15

    while '74' in str or '75' in str:
        if '75' in str:
            str = str.replace('75','744', 1)
        else:
            str = str.replace('74','44',1)
    if str.count('4') >= mx:
        mx = str.count('4')
print(n)

##ответ 15