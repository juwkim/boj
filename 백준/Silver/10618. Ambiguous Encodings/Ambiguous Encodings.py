import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    s = input()
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(1, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] = dp[i - 1]
        if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= 1 << 64
    print(f"Case #{tc}: {dp[-1]}")