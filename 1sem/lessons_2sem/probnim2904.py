# 2 task
# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if (not(x <= y) or (z == w) or z) == 0:
#                     print(w,x,y,z)

#задание 5

# def f(n):
#     troi = ''
#     n_copy = n
#     while n > 0:
#         troi = str(n % 3) + troi
#         n //= 3
#     if n_copy % 3 == 0:
#         troi = troi + troi[-2:]
#     else:
#         ost = 3*(n_copy % 3)
#         ost_3 = ''
#         while ost > 0:
#             ost_3 = str(ost % 3) + ost_3
#             ost //= 3
#         troi = troi + ost_3
#     return int(troi, 3)
#
# for n in range(1000, 1, -1):
#     if f(n) <= 150:
#         print(n)
#         break

# #6 задание
# from turtle import *
# k = 20
# left(90)
# screensize(2000, 2000)
# tracer(0)
#
# for _ in range(2):
#     forward(28*k)
#     right(90)
#     forward(18*k)
#     right(90)
# up()
# forward(14*k)
# right(90)
# forward(10*k)
# left(90)
# pd()
# for _ in range(2):
#     forward(30*k)
#     right(90)
#     forward(7*k)
#     right(90)
#
# pu()
#
# for x in range(-40, 40):
#     for y in range(-40, 60):
#         goto(x*k, y*k)
#         dot(5, 'red')
# done()


# # 8 задание
# from itertools import *
# cnt = 1
# for s in product(sorted('ПОБЕДА'), repeat=6):
#     ans = ''.join(s)
#     cnt += 1
#     if ans[0] == 'О' and ans.count(ans[1]) == 1 and ans.count(ans[2]) == 1 and ans.count(ans[3]) == 1 and ans.count(ans[4]) == 1 and ans.count(ans[5]) == 1:
#         print(cnt, ans)

#задание 12
#
# for n in range(4, 10000):
#     s = '4' + '2'*n
#     while '42' in s or '8222' in s or '2222' in s:
#         if '42' in s:
#             s = s.replace('42', '2', 1)
#         if '8222' in s:
#             s = s.replace('8222', '24', 1)
#         if '2222' in s:
#             s = s.replace('2222','8', 1)
#     if sum(int(x) for x in s) == 110:
#         print(n)
#         print(s)
#         break

# #задание 14
# max_zeros = -1
# best_x = 0
#
# for x in range(1, 3001):
#     num = 4**210 + 4**110 - x
#     chet = ''
#     n = num
#     while n > 0:
#         chet = str(n % 4) + chet
#         n = n // 4
#     zeros = chet.count('0')
#     if zeros > max_zeros:
#         max_zeros = zeros
#         best_x = x
#
# print(best_x)

def find_min_length(filename):
    with open(filename, 'r') as file:
        s = file.readline().strip()

    n = len(s)
    rsq_positions = []

    # Находим все позиции, где начинается RSQ
    for i in range(n - 2):
        if s[i] == 'R' and s[i+1] == 'S' and s[i+2] == 'Q':
            rsq_positions.append(i)

    if len(rsq_positions) < 130:
        return -1  # Недостаточно вхождений RSQ

    min_length = float('inf')

    # Перебираем все возможные последовательности из 130 вхождений
    for i in range(len(rsq_positions) - 129):
        start = rsq_positions[i]
        end = rsq_positions[i + 129] + 2  # +2 чтобы включить всю последнюю RSQ

        # Проверяем, что последовательность не заканчивается на Q
        if end + 1 < n and s[end + 1] == 'Q':
            continue

        current_length = end - start + 1
        if current_length < min_length:
            min_length = current_length

    return min_length if min_length != float('inf') else -1

# Пример использования
filename = 'z:24_21717.txt'  # Замените на имя вашего файла
result = find_min_length(filename)
print(f"Минимальная длина подстроки: {result}")
