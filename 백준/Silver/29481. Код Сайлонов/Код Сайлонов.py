import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, m = g()
A = [g() for _ in range(n)]
C11, C12, C21, C22 = g()
B = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        B[i][j] = (A[i - 1][j - 1] - B[i - 1][j - 1] * C11 - B[i - 1][j] * C12 - B[i][j - 1] * C21) // C22
for i in range(1, n + 1):
    print(*B[i][1:])