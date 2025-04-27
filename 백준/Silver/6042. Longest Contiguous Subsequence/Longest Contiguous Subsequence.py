import sys
input = sys.stdin.readline

L1, L2 = map(int, input().split())
S1 = [int(input()) for _ in range(L1)]
S2 = [int(input()) for _ in range(L2)]
dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
ans = 0
for i in range(1, L1 + 1):
    for j in range(1, L2 + 1):
        if S1[i - 1] == S2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])
print(ans)