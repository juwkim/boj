import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

mod = 1_000_000_007
D = int(input())
DP = [[0] * 8 for _ in range(2)]
cur, prv = 0, 1
DP[cur][0] = 1
for i in range(1, D + 1):
    cur ^= 1
    prv ^= 1
    DP[cur][0] = (DP[prv][1] + DP[prv][2]) % mod
    DP[cur][1] = (DP[prv][0] + DP[prv][2] + DP[prv][3]) % mod
    DP[cur][2] = (DP[prv][0] + DP[prv][1] + DP[prv][3] + DP[prv][4]) % mod
    DP[cur][3] = (DP[prv][1] + DP[prv][2] + DP[prv][4] + DP[prv][5]) % mod
    DP[cur][4] = (DP[prv][2] + DP[prv][3] + DP[prv][5] + DP[prv][7]) % mod
    DP[cur][5] = (DP[prv][3] + DP[prv][4] + DP[prv][6]) % mod
    DP[cur][6] = (DP[prv][5] + DP[prv][7]) % mod
    DP[cur][7] = (DP[prv][4] + DP[prv][6]) % mod
print(DP[cur][0])