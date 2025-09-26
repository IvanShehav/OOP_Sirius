clastersA = [[], []]

for s in open('7581a.txt'):
    s = s.replace(',', '.')
    x, y = [float(c) for c in s.split()]
    if x < 1:
        clastersA[0].append([x,y])
    else:
        clastersA[1].append([x,y])

clastersB = [[], [], []]

for s in open('7581b.txt'):
    s = s.replace(',', '.')
    x,y = [float(c) for c in s.split()]
    if y < 4:
        clastersB[0].append([x,y])
    elif x > 5:
        clastersB[1].append([x,y])
    else:
        clastersB[2].append([x,y])

def dist(p1, p2):
    x1,y1,x2,y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def center(claster):
    m = []
    for p in claster:
        sm = sum(dist(p, p1) for p1 in claster)
        m.append([sm,p])
    return min(m)[1]


centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]

pxA = sum(x for x,y in centerA)/2*10000
pyA = sum(y for x,y in centerA)/2*10000
print(int(pxA), int(pyA))

pxB = sum(x for x,y in centerB)/3*10000
pyB = sum(y for x,y in centerB)/3*10000
print(int(pxB), int(pyB))

#10738 30730
#37522 51277