from math import dist
a = [] # загрузка данных
for s in open('27-39b.txt'):
    if 'X' not in s:
        x,y = map(float,s.replace(',','.').split())
        a.append( (x,y) )

r = [] # 2й вариант DBSCAN
for p in a:
  r += [[p]]
  for c in r[:-1]:
    if any(dist(p,q)<0.7 for q in c):
      r[-1] += c
      r.remove(c)

# размеры кластеров
r.sort(key=len,reverse=1)
print(*map(len,r))

# центральные точки
xc = yc = 0
for c in r[:3]:
    s,(x,y) = min( (sum(dist(p,q) for q in c), p) for p in c)
    xc += x; yc += y

#диаметр(максимальное расстояние между точками одного кластера)
def diametr(cluster):
    max_dist = 0
    for i in range(len(cluster)):
        for j in range(i + 1, len(cluster)):
            d = dist(cluster[i], cluster[j])
            if d > max_dist:
                max_dist = d
    return max_dist
#радиус (среднее расстояние между точкми одного кластера)
def radius(cluster):
    total_dist = 0
    count = 0
    for i in range(len(cluster)):
        for j in range(i + 1, len(cluster)):
            total_dist += dist(cluster[i], cluster[j])
            count += 1
    return total_dist / count if count > 0 else 0
# min/max R между кластерами



print(int(abs(xc/3*10000)),int(abs(yc/3*10000)))

from turtle import *
tracer(0);up()
for c,cl in zip(r,('red green blue' + 'black'*100).split()):
  for x,y in c:
    goto(x*30,y*30); dot(3+7*(len(c) < 30),cl)
done()