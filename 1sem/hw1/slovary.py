string = input()

char = string[0]
length = 1

for i in string[1:]:
    if char == i:
        length += 1
    else:
        print(char, length)
        char = i
        length = 1
print(char,length)