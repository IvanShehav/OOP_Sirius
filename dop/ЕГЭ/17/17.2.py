A = [int(x) for x in open('17.txt')]
mn = 100001
res = []

for i in range(len(A)):
    if A[i] <= mn:
        mn = A[i]

for i in range(len(A)-1):
    if ((A[i] % 77) + (A[i+1] % 77)) == mn:
        res.append(A[i]+A[i+1])

print(len(res), max(res))