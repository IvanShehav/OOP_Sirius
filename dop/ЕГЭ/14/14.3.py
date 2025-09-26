##17-рчиная
alph = "0123456789ABCDEFG"
for x in alph:
    s1 = int(f'2AB{x}', 12)
    s2 = int(f'{x}8E', 17)
    s = s1 + s2
    if s % 27 == 0:
        print(s / 27)
        print(s)
        print(x)
        exit()