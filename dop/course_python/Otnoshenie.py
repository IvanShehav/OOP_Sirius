n = int(input())
ls = [int(x) for x in input().split()]

mn_val = ls[0]
mn_idx = 0
best_i = 0
best_j = 0
max_ratio = 1

for j in range(1, n):
    if ls[j] < mn_val:
        mn_val = ls[j]
        mn_idx = j
    ratio = ls[j] / mn_val
    if ratio > max_ratio and ratio > 1:
        max_ratio = ratio
        best_i = mn_idx
        best_j = j

if max_ratio > 1:
    print(best_i + 1, best_j + 1)
else:
    print(0, 0)