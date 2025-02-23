tf, tr, *l = map(float, open(0))
print(prv:=0)
for idx in range(1, len(l)):
    i = int(l[idx])
    r = l[idx] - i
    if 0 < l[idx] < 1:
        cur = 1
    elif r < tf:
        cur = i
    elif r > tr:
        cur = i + 1
    elif prv < i + tr:
        cur = i
    else:
        cur = i + 1
    print(prv:=cur)