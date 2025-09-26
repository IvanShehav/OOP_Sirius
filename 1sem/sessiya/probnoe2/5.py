for a in range(1,100):
    flag = True
    for x in range(100):
        for y in range(100):
            flag *= (((x < 10) <= (y > 40)) or not((y < a) <= (x > a)))
    if flag:
        print(a)
        break
