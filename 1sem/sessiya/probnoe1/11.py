res = []

for i in range(123456789, 223456789 + 1):
    delit = []
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0:
            delit.append(x)
            if len(delit) > 3:
                break
            if x != i // x:
                delit.append(i // x)

    if len(delit) == 3:
        res.append(max(delit))

print(sorted(res))
