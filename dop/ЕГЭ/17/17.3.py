A = [int(x) for x in open('17.txt')]
mx = -100*10**6
res = []

for num in A:
    if abs(num) % 100 == 21 and len(str(abs(num))) == 5:
        if num > mx:
            mx = num

for i in range(len(A)-1):
    c = 0
    if abs(A[i]) % 100 == 21 and len(str(abs(A[i]))) == 5:
        c += 1
    if abs(A[i+1]) % 100 == 21 and len(str(abs(A[i+1]))) == 5:
        c += 1
    if c == 1 and ((A[i]**2) + (A[i+1]**2)) >= mx**2:
        res.append(A[i]+A[i+1])
print(len(res), max(res))