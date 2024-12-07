from bisect import bisect_left

input()
dp = [0]
for A in map(int, input().split()):
    if A > dp[-1]:
        dp.append(A)
    else:
        dp[bisect_left(dp, A)] = A
print(len(dp) - 1)