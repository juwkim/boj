import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

M, L, S = g()
P = [int(input()) for _ in range(M)]

ans = float("inf")
for i in range(M - 1):
    t1 = P[i] + S * (i + 1)
    t2 = L - P[i + 1] + S * (M - i - 1)
    ans = min(ans, max(t1, t2))

t1, t2 = P[M - 1] + S * M, 0
ans = min(ans, max(t1, t2))

t1, t2 = 0, L - P[0] + S * M
ans = min(ans, max(t1, t2))

print(ans)