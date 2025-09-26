# num = input()
# count = 1
# number = num[0]
#
# for i in num[1:]:
#     if number == i:
#         count += 1
#     else:
#         print(number, count)
#         count = 1
#         number = i
# print(number, count)
#
#




numbers = input().split()
res = []

for num in numbers:
    if num.isdigit():
        res.append(int(num))
    else:
        b = res.pop()
        a = res.pop()

        if num == '+':
            result = a + b
        elif num == '-':
            result = a - b
        elif num == '*':
            result = a * b

        res.append(result)

print(res.pop())

