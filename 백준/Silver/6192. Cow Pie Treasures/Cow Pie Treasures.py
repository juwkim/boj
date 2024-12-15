g = lambda: [*map(int, input().split())]

R, C = g()
A = [g() for _ in range(R)]
DP = [[0] * (C + 1) for _ in range(R + 2)]
for j in range(C):
    for i in range(min(R, j + 1)):
        DP[i + 1][j + 1] = max(DP[i][j], DP[i + 1][j], DP[i + 2][j]) + A[i][j]
print(DP[R][C])