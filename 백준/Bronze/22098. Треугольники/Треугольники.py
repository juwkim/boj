from itertools import combinations
for _ in range(int(input())):
    x, y, z = 0, 0, 0
    l = sorted(map(int, input().split()))
    for p, q, r in combinations(l, 3):
        if p + q <= r:
            continue
        if p*p + q*q == r*r:
            x += 1
        elif p*p + q*q > r*r:
            y += 1
        else:
            z += 1
    print(x, y, z)