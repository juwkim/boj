import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
A = [g() for _ in range(N)]
ans = sum(sum(l) for l in A)
if N % 2 == 0 and M % 2 == 0:
    ans -= min(A[i][j] for i in range(N) for j in range(i%2==0, M, 2))
print(ans)