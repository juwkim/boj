mod = 1_000_000_007
N = int(input())
d = [[1] * (N + 1) for _ in range(N + 1)]
for i in range(1, 1 + N):
    for j in range(1, 1 + N):
        d[i][j] = (d[i-1][j] + d[i][j-1]) % mod
print(d[N][N], N ** 2 % mod)