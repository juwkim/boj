import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
px = [0] * (N + 1)
for i, a in enumerate(g(), 1):
    px[i] = px[i - 1] ^ a
ans = 0
for _ in range(Q):
    s, e = g()
    ans ^= px[e] ^ px[s - 1]
print(ans)