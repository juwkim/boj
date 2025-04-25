import sys
input = sys.stdin.readline
from itertools import product

N, K = map(int, input().split())
same, diff = [], []
for _ in range(K):
    t, x, y = input().split()
    x, y = int(x) - 1, int(y) - 1
    if t == 'S':
        same.append((x, y))
    else:
        diff.append((x, y))
ans = 0
for p in product(range(3), repeat=N):
    ok = True
    for x, y in same:
        if p[x] != p[y]:
            ok = False
            break
    if not ok:
        continue
    for x, y in diff:
        if p[x] == p[y]:
            ok = False
            break
    if ok:
        ans += 1
print(ans)