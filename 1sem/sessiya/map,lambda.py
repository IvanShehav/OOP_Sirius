# a = [12, 13, -142, 23, -131, 24]
# c = list(map(lambda x: len(str(abs(x))), a))
# b = list(map(lambda x: abs(x) // 10**(len(str(abs(x)))-1), a))
# print(c,b, sep='\n')

# map(func, *iterators)
# lambda x: x**2

# def sum_two_number(x, y):
#     return x + y
#
# print(sum_two_number(1, 90))
# ans = list(map(sum_two_number, {1, 2, 3}, [1, 90]))
# print(ans)

s = 'abcdefecbadfabcfabd'
a = {x:0 for x in 'abcdef'}
print(a)
for el in s:
    a[el] += 1
print(a)