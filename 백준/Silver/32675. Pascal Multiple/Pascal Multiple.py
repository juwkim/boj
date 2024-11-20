from itertools import pairwise

N, K = map(int, input().split())
ans, cur = (2 * N + 1) * (K == 1), (1,)
for _ in range(N):
    cur = [1] + [(a + b) % K for a, b in pairwise(cur)] + [1]
    ans += cur.count(0)
print(ans)