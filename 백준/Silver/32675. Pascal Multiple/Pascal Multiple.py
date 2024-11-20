from itertools import pairwise

N, K = map(int, input().split())
ans = (0, 2 * N + 1)[K == 1]
cur = (1, 1)
for i in range(2, N + 1):
    nxt = [1]
    for a, b in pairwise(cur):
        nxt.append(num := (a + b) % K)
        ans += num == 0
    nxt.append(1)
    cur = nxt
print(ans)