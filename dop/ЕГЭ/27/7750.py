#алгоритмом DBscan

f = open('7750b.txt')
f.readline()

data = []
for s in f:
    s = s.replace(',','.')
    p = [float(c) for c in s.split()]
    data.append(p)

#кластеризация

def dist(p1, p2):
    x1,y1,x2,y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def getCluster(p0):
    cluster = [p for p in data if dist(p0,p) < 0.2]
    if len(cluster) > 0:
        for p in cluster: data.remove(p)
        next_cluster = [getCluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster


#разбиение

clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    clusters.append(cluster)

k = len(clusters)

def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p,p1) for p1 in kl)
        m.append([s,p])
    return min(m)[1]

centroid = [center(kl) for kl in clusters]


Px = sum(x for x,y in centroid)/k*10000
Py = sum(y for x,y in centroid)/k*10000
print(int(Px), int(Py))


#36305 54432
#41821 49335

