import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M = g()
A = [g() for _ in range(N)]
B = [g() for _ in range(N)]
ans = 0
best = [-1] * N
for b in g():
    b -= 1
    if best[b] == -1:
        best[b] = max(range(N), key=lambda i: abs(A[i][b] - B[i][b]))
    a = best[b]
    ans += abs(A[a][b] - B[a][b])
print(ans)