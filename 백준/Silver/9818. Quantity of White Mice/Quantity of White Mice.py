import sys
input = lambda: sys.stdin.readline().rstrip()

while (s:=input()) != '-1':
    n, m, k = map(int, s.split(','))
    dp = [1] + [0] * (n - 1)
    for _ in range(k - 1):
        dp = [0] + dp[:-1]    
        if sum(dp) <= 100:
            dp[0] = dp[6] + dp[7] + 2 * sum(dp[8:8+m])
    print(f"{s}: {sum(dp)}")