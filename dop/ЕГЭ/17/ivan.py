numbers = [int(x) for x in open('17.txt')]
max_n = 0

for num in numbers:
    if len(str(abs(num))) == 3 and num % 10 == 3 and num > max_n:
        max_n = num

q = 0
max_sum = -100000 * 2

for i in range(len(numbers) - 2):
    pair = numbers[i:i + 3]

    if [num % 10 == 3 and len(str(abs(num))) == 3 for num in pair].count(True) >= 1:
        if sum(pair) < max_n:
            q += 1

            if sum(pair) > max_sum:
                max_sum = sum(pair)

print(q, max_sum)





