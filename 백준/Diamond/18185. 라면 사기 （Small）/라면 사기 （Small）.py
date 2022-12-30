input = __import__('sys').stdin.readline

N = int(input())
nums = [*map(int, input().split())]
dp = [[max(0, nums[0] - nums[1]), 0, 0], [max(0, nums[1] - nums[0]), min(nums[:2]), 0]]
for i in range(2, N):

    buf = [0, 0, 0]
    for k in range(2):
        num = min(dp[i-1][k], nums[i])
        buf[k + 1] = num
        dp[i-1][k] -= num
        nums[i] -= num
    
    buf[0] = nums[i]
    dp.append(buf)

ans = 0
for a, b, c in dp:
    ans += 3 * a + 5 * b + 7 * c
print(ans)