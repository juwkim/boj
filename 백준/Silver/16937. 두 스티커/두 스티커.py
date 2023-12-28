import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import combinations

H, W = g()
N = int(input())
buf = [g() for _ in range(N)]
ans = 0
for (r1, c1), (r2, c2) in combinations(buf, 2):
    if r1 + r2 <= H:
        if c1 <= W and c2 <= W:
            ans = max(ans, r1 * c1 + r2 * c2)
    if r1 + r2 <= W:
        if c1 <= H and c2 <= H:
            ans = max(ans, r1 * c1 + r2 * c2)
    if r1 + c2 <= H:
        if c1 <= W and r2 <= W:
            ans = max(ans, r1 * c1 + r2 * c2)
    if r1 + c2 <= W:
        if c1 <= H and r2 <= H:
            ans = max(ans, r1 * c1 + r2 * c2)
    if c1 + r2 <= H:
        if r1 <= W and c2 <= W:
            ans = max(ans, r1 * c1 + r2 * c2)
    if c1 + r2 <= W:
        if r1 <= H and c2 <= H:
            ans = max(ans, r1 * c1 + r2 * c2)
    if c1 + c2 <= H:
        if r1 <= W and r2 <= W:
            ans = max(ans, r1 * c1 + r2 * c2)
    if c1 + c2 <= W:
        if r1 <= H and r2 <= H:
            ans = max(ans, r1 * c1 + r2 * c2)
print(ans)