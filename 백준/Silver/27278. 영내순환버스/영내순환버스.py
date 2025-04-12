import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
px = [0] * (N + 2)
for i, t in enumerate(g(), 1):
    px[i + 1] = px[i] + t
ans, time = 0, px[-1]
for _ in range(M):
    p, r, c = g()
    ans = max(ans, (c + time - px[p] - 1) // time * time + px[p] + (px[r] - px[p]) % time)
print(ans)