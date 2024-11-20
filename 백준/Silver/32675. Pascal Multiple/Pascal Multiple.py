from itertools import pairwise

N, K = map(int, input().split())
ans = (2 * N + 1) * (K == 1)
cur = (1, 1)
for i in range(2, N + 1):
    cur = [1] + [(a + b) % K for a, b in pairwise(cur)] + [1]
    ans += cur.count(0)
print(ans)