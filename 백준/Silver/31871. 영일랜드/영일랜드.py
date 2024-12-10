import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
cost = [[-1] * (N + 1) for _ in range(N + 1)]
for _ in range(int(input())):
    u, v, d = map(int, input().split())
    cost[u][v] = max(cost[u][v], d)

ans = -1
for p in permutations(range(1, N + 1)):
    p = [0] + list(p) + [0]
    cur = 0
    for i in range(N + 1):
        if cost[p[i]][p[i + 1]] == -1:
            cur = -1
            break
        cur += cost[p[i]][p[i + 1]]
    ans = max(ans, cur)
print(ans)