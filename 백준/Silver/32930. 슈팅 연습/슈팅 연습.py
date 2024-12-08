import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
dist2 = lambda p1, p2: (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

N, M = g()
A = [g() for _ in range(N)]
ans, x, y = 0, 0, 0
for _ in range(M):
    idx = max(range(N), key=lambda i: dist2(A[i], (x, y)))
    ans += dist2(A[idx], (x, y))
    x, y = A.pop(idx)
    A.append(g())
print(ans)