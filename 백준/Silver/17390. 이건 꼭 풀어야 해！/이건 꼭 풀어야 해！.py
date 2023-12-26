import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, Q = g()
px = [0] * (N + 1)
for idx, num in enumerate(sorted(g())):
    px[idx + 1] = px[idx] + num
for _ in range(Q):
    L, R = g()
    ans = px[R] - px[L - 1]
    print(ans)