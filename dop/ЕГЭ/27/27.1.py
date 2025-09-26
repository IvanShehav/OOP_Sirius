from math import dist
a = [] # загрузка данных
for s in open('z:27_B_20816.txt'):
  x,y = map(float,s.replace(',','.').split())
  a.append( (x,y) )

r = [] # 2й вариант DBSCAN
for p in a:
  r += [[p]]
  for c in r[:-1]:
    if any(dist(p,q)<2 for q in c):
      r[-1] += c
      r.remove(c)

# размеры кластеров
r.sort(key=len,reverse=1)
print(*map(len,r))

# центральные точки
xc = yc = 0
for c in r:
  s,(x,y) = min( (sum(dist(p,q) for q in c), p) for p in c)
  xc += x; yc += y
print(int(abs(xc/3*10000)),int(abs(yc/3*10000)))

from turtle import *
tracer(0);up()
for c,cl in zip(r,'red green blue'.split()):
  for x,y in c:
    goto(x*30,y*30); dot(3,cl)
