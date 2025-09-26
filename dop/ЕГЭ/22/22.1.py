d = {0:0}
for s in open('data.txt'):
    r = s.replace(';', ' ').split()
    i,t,*z = map(int, r)
    d[i] = max(d[t1] for t1 in z) + t
print(max(d.values()))