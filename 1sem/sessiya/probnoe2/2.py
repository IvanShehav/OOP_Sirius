n = int(input())
toys = []
unique = []
for i in range(n):
    name, strr = input().split(': ')
    toys.extend(set(strr.split(', ')))
for i in range(len(toys)):
    toy = toys.pop(0)
    if toy not in toys:
        unique.append(toy)
    toys.append(toy)
print('\n'.join(sorted(unique)))