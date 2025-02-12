x1, x2, x3 = map(int, input().split())
m = max(x1, x2, x3)
if x1 + x2 + x3 == m << 1:
    print(0)
else:
    if x1 == m:
        print(1)
        diff = x2 - x3
    elif x2 == m:
        print(2)
        diff = x3 - x1
    else:
        print(3)
        diff = x1 - x2
    print(m - diff >> 1, m + diff >> 1)