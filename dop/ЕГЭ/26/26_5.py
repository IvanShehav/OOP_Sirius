m = open("26_5.txt").read().split("\n")
m.pop(0)
mass = []
for t in m:
    mass.append(list(map(int, t.split())))
mass = sorted(mass, key = lambda x: (x[0], sum(x[1:])))