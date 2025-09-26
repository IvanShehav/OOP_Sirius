from itertools import *

cnt = 0
# glas = 'ИУ'
# sogl = 'МНС'
# mx = 0
# for i in product('ИМНСУ', repeat=4):
#     a = ''.join(i)
#     cnt += 1
#     # if a == 'УУСС':
#     #     print(a, cnt)
#     #     break
#     c_sogl = 0
#     c_glas = 0
#     for j in i:
#         if j in sogl:
#             c_sogl +=1
#         else:
#             c_glas += 1
#     if c_sogl >= c_glas and cnt > mx:
#         mx = cnt
# print(mx)

# for i in product('АКМСУ', repeat=5):
#     a = ''.join(i)
#     cnt += 1
#     if a == 'КУМАС':
#         print(cnt)
#         break

# for i in product('БГДНОУШ', repeat=6):
#     a = ''.join(i)
#     cnt += 1
#     if a == 'ШШШШНН':
#         print(cnt)
#         break

for i in product('СПОЛКЙЕ', repeat=6):
    a = ''.join(i)
    cnt += 1
    if a[0] == 'К' and a.count('Й') >= 2 and a.count('С') == 0 and a.count('Е') == 0:
        if (cnt-1) % 2 == 0:
            print(cnt-1)
            break

