str = '5' * 874

while '555' in str or '111' in str:
    if '555' in str:
        str = str.replace('555', '1', 1)
    else:
        str = str.replace('111','5',1)
print(str.count('5'))
print(str)