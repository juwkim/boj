import sys
input = sys.stdin.readline
from itertools import combinations, product

T = int(input())
point = [0, 0, 0, 0, 0]
l = {*combinations(range(1, 5), 2)}
for _ in range(int(input())):
    A, B, SA, SB = map(int, input().split())
    l.remove((A, B))
    if SA > SB:
        point[A] += 3
    elif SA < SB:
        point[B] += 3
    else:
        point[A] += 1
        point[B] += 1
ans = 0
l = list(l)
for p in product(((3, 0), (0, 3), (1, 1)), repeat=len(l)):
    cur = point[:]
    for (A, B), (PA, PB) in zip(l, p):
        cur[A] += PA
        cur[B] += PB
    m = max(cur)
    if cur[T] == m and cur.count(m) == 1:
        ans += 1
print(ans)