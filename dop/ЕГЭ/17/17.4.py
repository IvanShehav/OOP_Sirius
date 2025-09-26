A = [int(x) for x in open('17.txt')]
mx = -100*10**6
res = []

for num in A:
    if len(str(abs(num))) == 3:
        if num > mx:
            mx = num

for i in range(len(A)-1):
    if (len(str(A[i])) == 3 and len(str(A[i+1])) != 3) or (len(str(A[i])) != 3 and len(str(A[i+1])) == 3):
        if (A[i]+A[i+1]) % mx == 0:
            res.append(A[i]+A[i+1])
print(len(res), max(res))