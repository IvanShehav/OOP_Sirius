##32-ричная
alph = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
for x in alph:
    s1 = int(f'931{x}964', 32)
    s2 = int(f'4{x}51{x}1', 32)
    s3 = int(f'2861{x}637', 32)
    s = s1 + s2 + s3
    if s % 31 == 0:
        print(s/31)
        print(s)
        exit()