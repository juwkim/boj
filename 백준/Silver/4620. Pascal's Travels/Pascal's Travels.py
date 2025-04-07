import sys
input = lambda: sys.stdin.readline().rstrip()

while (n:=int(input())) != -1:
    a = [[*map(int, input())] for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                continue
            if i + a[i][j] < n:
                dp[i + a[i][j]][j] += dp[i][j]
            if j + a[i][j] < n:
                dp[i][j + a[i][j]] += dp[i][j]
    print(dp[-1][-1])