def tracking(A, B, x, y):
    LCS = ""
    while dp[x][y] != 0:
        if dp[x][y] == dp[x-1][y]:
            x -= 1
        elif dp[x][y] == dp[x][y-1]:
            y -= 1
        else:
            LCS = A[x] + LCS
            x -= 1
            y -= 1
    return LCS

A, B = " " + input(), " " + input()
dp = [[0 for i in range(len(B))] for j in range(len(A))]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])
if dp[-1][-1]:
    print(tracking(A, B, -1, -1))