from random import randint

# A = [randint(0,101) for x in range(2)]
# sum_min = 0
# for x in A:
#     sum += x
#
# print(*A)
# print(sum/len(A))

# A = [randint(0,5) for x in range(4)]
# num = int(input())
# flag = False
# for i in range(len(A)):
#     if A[i] == num:
#         flag = True
#         print(f'A[{i + 1}]={num}', sep = ', ')
#     if not flag:
#         print("Ничего нет")

lst = [randint(0,5) for i in range(10)]
# x_prev = list[0]
# ans = []
#
# for x in lst[1:]:
#     if x == x_prev:
#         ans.append(x)
#     x_prev = x
# if len(ans) != 0:
#     print(f'Есть: {ans}')
# else:
#     print('Нет')
pov_el = []
for i in range(1, len(lst)):
    if lst[i] in lst[:i-1]:
        pov_el.append(lst[i])
if len(pov_el) > 0:
    print(f'Есть: ')