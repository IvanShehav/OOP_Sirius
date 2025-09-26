lst = set()

for _ in range(int(input())):
    if (el := input()) not in lst:
        lst.add(el)

for _ in range(int(input())):
    for _ in range(int(input())):
        if (el := input()) in lst:
            lst.remove(el)

menu = sorted(lst)

if not menu:
    print('Готовить нечего')
else:
    for el in menu:
        print(el)