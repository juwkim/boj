import sys
input = sys.stdin.readline
LCS = 0
A, B = " " + input().rstrip(), " " + input().rstrip()
dp = [[0 for i in range(len(B))] for j in range(len(A))]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            LCS = max(LCS, dp[i][j])
print(LCS)