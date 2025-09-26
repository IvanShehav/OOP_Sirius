count_simbol = int(input())
count_str = int(input())
count_s = 0

str = []

res = []


for i in range(count_str):
    str.append(input())

for i in range(count_str):
    count_s += len(str[i])
    if count_s >= count_simbol:
        print(str[i][:count_simbol-3] + '...')
        exit()
    else:
        print(str[i])

