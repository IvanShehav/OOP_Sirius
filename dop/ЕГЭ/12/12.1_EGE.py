mx_sum = 0
for n in range(4, 10000):
    str = '1' + '9'*n
    while '19' in str or '49' in str or '999' in str:
        if '19' in str:
            str = str.replace('19','9',1)
        if '49' in str:
            str = str.replace('49','91',1)
        if '999' in str:
            str = str.replace('999','4',1)
    sum_num = str.count('1') + str.count('9')*9 + str.count('4')*4
    if sum_num >= mx_sum:
        mx_sum = sum_num
print(mx_sum)