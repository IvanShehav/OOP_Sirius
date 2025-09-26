A = [int(x) for x in open('17.txt')]
mx = 0
res = []

for i in range(len(A)):
    if abs(A[i]) % 10 == 3 and len(str(abs(A[i]))) == 3:
        if A[i] >= mx:
            mx = A[i]
print(mx)

for i in range(len(A)-2):
    if (abs(A[i]) % 10 == 3 and len(str(abs(A[i]))) == 3) or (abs(A[i+1]) % 10 == 3 and len(str(abs(A[i+1]))) == 3) or (abs(A[i+2]) % 10 == 3 and len(str(abs(A[i+2]))) == 3):
        if (A[i]+A[i+1]+A[i+2]) < mx:
            res.append(A[i]+A[i+1]+A[i+2])

print(len(res), max(res))


