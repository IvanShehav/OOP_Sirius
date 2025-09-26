#сортируем список гирь по убыванию
#сортируем список спортсенов по убыванию
#список подсчета гирь где все жлементы = 0 а количесвто = длине весов
# пока число из гирь меньше вес, то сравниваем, как только нашли подходящую накапливаем в сумму, а индекс

# f = open('_TFh-NDjqE.txt')
# n, m = map(int, f.readline().split())
# w = sorted([int(f.readline()) for i in range(n)], reverse=True) #гири
# w_max = sorted([int(f.readline()) for j in range(m)], reverse=True) #спортмены
# s = 0
# i = 0
# count = [0]*n
# for x in w_max:
#     while x < w[i]:
#         i += 1
#     s += w[i]
#     count[i] += 1
# median = s // m
# max_w = count.index(max(count))
#
# print(median, w[max_w])



##

# f = open('26_2.txt')
# n, m = map(int, f.readline().split())
# student = []
# for i in range(n):
#     student.append([int(x) for x in f.readline().split()])
# seans = sorted([int(f.readline()) for i in range(m)])
# student.sort(key = lambda x: (-x[1], x[0], x[2]))
# count_p = 0
# count_student = 0
# for st in student:
#     for i in range(m): #проходимся по длине сеансов
#         if st[2] <= seans[i]:
#             seans[i] = -1
#             count_p += st[2]
#             count_student += 1
#             break
# print(count_student, count_p)


