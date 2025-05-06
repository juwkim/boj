import sys
input = sys.stdin.readline

MOD = 10**9 + 9
MAXN = 100000
u = [1, 1] + [0] * (MAXN - 1)
d = [1, 1, 2, 4] + [0] * (MAXN - 3)
for i in range(2, MAXN + 1):
    u[i] = (u[i - 1] + u[i - 2]) % MOD
for i in range(4, MAXN + 1):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3] + d[i - 4]) % MOD
for _ in range(int(input())):
    input()
    n = int(input())
    print(u[n] * d[n] % MOD)