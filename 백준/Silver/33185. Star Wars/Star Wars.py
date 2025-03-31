n, m = map(int, input().split())
lines = [input() for _ in range(n - 1)]
dp = [-1] + [(-1, 0)[c == 'W'] for c in input()] + [-1]
ans = 0
for line in lines[::-1]:
    new_dp = [-1] * (m + 2)
    for j, c in enumerate(line, 1):
        if c == 'W':
            new_dp[j] = 0
        else:
            nums = [num for num in dp[j-1:j+2] if num != -1]
            if nums:
                new_dp[j] = max(nums) + (c == 'B')
    dp = new_dp
    ans = max(ans, max(dp))
print(ans)