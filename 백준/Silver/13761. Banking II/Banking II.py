PIN = [*map(int, input())]
pattern = [ord(c) - ord('a') + 1 for c in input()]
dp = [[-1] * (len(PIN) + 1) for _ in range(len(pattern) + 1)]

def solve(i, j, num):
    if num <= dp[i][j]:
        return
    dp[i][j] = num
    if i == len(pattern):
        return
    for k in range(j, len(PIN) + 1 - pattern[i] - sum(pattern[i+1:])):
        solve(i + 1, k + pattern[i], num + sum(PIN[k:k + pattern[i]]))
    
solve(0, 0, 0)
print(max(dp[-1]))