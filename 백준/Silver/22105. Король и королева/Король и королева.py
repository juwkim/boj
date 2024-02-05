import sys
input = sys.stdin.readline
from itertools import product

for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    ans = []
    for d1, d2 in product((x - 1, n - x), (y - 1, m - y)):
        k1, k2 = max(d1 - d2, 0), max(d2 - d1, 0)
        p1, p2 = (d1 + k1 - 1) * (d1 - k1) // 2, (d2 + k2 - 1) * (d2 - k2) // 2
        if p1:
            ans.append(p1)
        if p2:
            ans.append(p2)
    print(len(ans), *sorted(ans))