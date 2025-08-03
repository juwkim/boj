N, K, M = map(int, input().split())
allowed = [[True] * K for _ in range(K)]

for i in range(K):
    allowed[i][i] = False

for _ in range(M):
    idxs = [ord(c) - ord('A') for c in input()]
    for a in idxs:
        for b in idxs:
            allowed[a][b] = False

dp = [[0] * K for _ in range(N)]
for i in range(K):
    dp[0][i] = 1

for pos in range(1, N):
    for cur in range(K):
        dp[pos][cur] = sum(dp[pos - 1][prv] for prv in range(K) if allowed[prv][cur])
print(sum(dp[N-1]))