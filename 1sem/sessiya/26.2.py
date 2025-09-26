f = open('1_26.1.txt')
l, p, n = (int(x) for x in f.readline().split())
orders = [list(map(int, x.split())) for x in f.readlines()]
orders.sort(reverse=True, key = lambda x: [x[0], x[2], x[1]])
eval = {}
for lot, user, price in orders:
    if lot not in eval.keys():
        eval[lot] = 0
    else:
        if eval[lot] == 0:
            eval[lot] = price
r = [(x,y) for x, y in eval.items() if y  != 0]
print(len(r), sum(eval.values()))