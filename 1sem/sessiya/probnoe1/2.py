n = int(input())
dic = dict()
for i in range(n):
    a = input().split(':')
    b = a
    names = a[0]
    a.pop(0)
    dic[f'{names}'] =