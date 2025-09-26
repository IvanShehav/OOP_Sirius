# f = open('1_26.1.txt')
# n, m = (int(x) for x in f.readline().split())
#
# lst = []
# for i in range(n):
#     a, b = (x for x in f.readline().split())
#     lst.append([a, b])
# lst.sort()
# count = 0
# cnt_q = 0
# index = 0
# sum_z = []
# sum_q = []
# while count < m:
#     if count + int(lst[index][0]) > m:
#         index += 1
#         break
#     count += int(lst[index][0])
#     if lst[index][1] == 'Q':
#         sum_q.append(lst[index][0])
#     else:
#         sum_z.append(lst[index][0])
#
#     index += 1
# ostatok = m - count
# # print(len(sum_q)+len(sum_z))
# # print(len(sum_q))
# while True:
#     while lst[index][1] != 'Q' and index < len(lst):
#         index += 1
#     raznica = int(lst[index][0]) - int(sum_z[-1])
#     if raznica < ostatok:
#         sum_q.append(lst[index][0])
#         sum_z.pop()
#         ostatok -= raznica
#     else:
#         break
# print(len(sum_q), ostatok)
# # # # print(lst[index])
# # # # print(lst[index-10:index+10])
# # # # print(sum_z[-1])
# # # # print(len(sum_q)+len(sum_z))
# # # # print(lst[index-10:index+10])
# # # # print(cnt_q, m-count)
#
# 

"""#### =============РАЗБОР==================####"""
# f = open('1_26.1.txt')
# n, m = (int(x) for x in f.readline().split())
#
# lst = []
# for i in range(n):
#     a, b = (x for x in f.readline().split())
#     lst.append([a, b])
# lst.sort()
#
# lst_q = []
# lst_z = []
# i = 0
#
# while m >= 0:
#     if (m - int(lst[i][0])) < 0:
#         break
#
#     if lst[i][1] == 'Q':
#         lst_q.append(lst[i][0])
#     else:
#         lst_z.append(lst[i][0])
#
#     m -= int(lst[i][0])
#     i += 1
#
# # print(lst_q, lst_z, m, sep = '\n')
#
#
# while True:
#     while lst[i][1] != 'Q':
#         i += 1
#
#     zp = int(lst_z.pop())
#
#     if m + zp - int(lst[i][0]) >= 0:
#         m = m + zp - int(lst[i][0])
#         lst_q.append(lst[i][0])
#     else:
#         break
#     i += 1
#
# print(len(lst_q), m)























