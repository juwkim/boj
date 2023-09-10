import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
A = g()
for i in range(1, N):
    A[i] += A[i - 1]

ans = sum(sorted(A)[-K:])
print(ans)