for n1 in range(50):
    for n2 in range(50):
        for n3 in range(50):
            s = '0' + n1*'1' + n2*'2' + n3*'3'

            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01','30', 1)
                s = s.replace('02','3103', 1)
                s = s.replace('03','1201', 1)
            if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
                       print((n1))
                       exit()