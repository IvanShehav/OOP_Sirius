count_zapr = int(input())
for i in range(count_zapr):
    p, a = map(int, input().split())
    print(pow(a, p-2, p))
