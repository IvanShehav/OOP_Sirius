#ДУМАТЬ НЕ НАДО
# def f(a, s, n):
#     if a+s >= 123: return n % 2 == 0
#     if n < 0: return 0
#     h = [f(a*2,s,n-1), f(a+2,s,n-1), f(a,s*2,n-1),f(a,s+2,n-1)]
#     return any(h) if n % 2 != 0 else all(h)
#
# for s in range(1,110):
#     if f(13,s,2):
#         print(s)


#способ множествами

# def h(s): return s-2, s-5, s//3
#
# g = {*range(20, 20*3**4+1)}
#
# w1 = {s for s in g if any(t < 20 for t in h(s))}
# l1 = {s for s in g if all(t in w1 for t in h(s))}
# g = g - l1 - w1
# w2 = {s for s in g if any(t in l1 for t in h(s))}
# w12 = w1 | w2
# l2 = {s for s in g if all(t in w12 for t in h(s))}
#
# print(min(l1))
# print(*sorted(w2)[:2])
# print(min(l2))


# def h(a,b): return (a-2,b-2), (a//2,b), (a,b//2)
#
# g = {(a,b) for a in range(1000) for b in range(1000) if a+b>37}
# w1 = {p for p in g if any(sum(t) <= 37 for t in h(*p))}
# l1 = {p for p in g if all(t in w1 for t in h(*p))}
# g = g - l1 - w1
# w2 = {p for p in g if any(t in l1 for t in h(*p))}
# w12 = w1 | w2
# l2 = {p for p in g if all(t in w12 for t in h(*p))}
#
# print(min(s for s in range(25, 999) if (24,s) in l1))
#
# r20 = {s for s in range(25,9999) if (s,24) in w2}
#
# print(min(r20), max(r20))
# print(min(s for s in range(25,9999) if (s,24) in l2))


#Код с использование рекурсии

# def f(s,m): return 1-m%2 if s >= 301 else m and [all,any][m%2]([f(s+3,m-1),f(s*5,m-1)])
#
# for m, F in enumerate((min,list,min)):
#     print(F(s for s in range(301) if f(s,m+2) > f(s,m)))



from itertools import *
# count = 0
# for i in product(sorted(set('МАРИНА')), repeat=8):
#     count += 1
#     s = ''.join(i)
#     if s == 'МАРИАННА':
#         print(count,s)
#     # print(count, s)

# cnt = 0
# lst = []
# name = sorted(set('МАРИНА'))
# for j in permutations ('МАРИ'):
#     s = ''.join(j)
#     for i in product('ИНА', repeat=4):
#         s1 = ''.join(i)
#         s2 = s + s1
(';p['
 '/')#         lst.append(s2)
# lst.sort()
# print(lst.index('МАРИАННА')+1)
# # for i in lst:
# #     cnt += 1
# #     if i == 'МАРИАННА':
# #         print(cnt,i)
#         # print(count, s)

# #17873
# from itertools import *
# file = [*map(int,open('17.txt'))]
# m = min(file)
# b = [x+y for x,y in pairwise(file) if x % 16 == m or y%16 == m] #pairwise перебирает пары
# print(len(b), max(b))


alph = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
alph2 = list(''.join(s) for s in product(alph, repeat=2))
print(alph2)