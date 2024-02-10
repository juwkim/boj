import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    P = [*map(float, input().split())]
    dp = [(P[0], 0)]
    if n >= 2:
        dp.append((P[1], max(dp[-1])))
    if n >= 3:
        dp.append((P[2], max(dp[-1])))
    for i in range(3, n):
        dp.append((P[i] + max(dp[i-3]), max(dp[-1])))
    print(max(dp[-1]))