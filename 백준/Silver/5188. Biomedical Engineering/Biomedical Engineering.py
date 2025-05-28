import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, int(input()) + 1):
    m = int(input())
    n = len(z:=input())
    primitives = [input() for _ in range(m)]
    dp = [0] + [1e9] * n
    for i in range(1, n + 1):
        for y in primitives:
            l = len(y)
            if z[i-l:i] == y:
                dp[i] = min(dp[i], dp[i - l] + 1)
    print(f"Data Set {tc}:")
    if dp[n] == 1e9:
        print("Impossible")
    else:
        print(dp[n])