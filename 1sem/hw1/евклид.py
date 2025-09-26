string = input().split()

numbers = []

for digits in string:
    numbers.append(int(digits))

current_gcd = numbers[0]

for number in numbers[1:]:
    while number != 0:
        current_gcd, number = number, current_gcd % number

print(current_gcd)