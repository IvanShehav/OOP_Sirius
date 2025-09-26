##19-рчиная
alph = "0123456789ABCDEFGHI"
for x in alph[::-1]:
    s1 = int(f'98897{x}21', 19)
    s2 = int(f'2{x}923', 19)
    s = s1 + s2
    if s % 18 == 0:
        print(s / 18)
        print(s)
        exit()