def factor(num, ans=2, k=0, dsum=0):
    while ans * ans <= num:
        if num % ans == 0:
            k += 1
            dsum += ans
            if ans != num // ans:
                k += 1
                dsum += num // ans
        ans += 1
    return 0 if k == 0 else dsum // k


cnt = 5
n = 550000
while cnt:
    F = factor(n)
    if F % 31 == 13:
        print(n, F)
        cnt -= 1
    n += 1