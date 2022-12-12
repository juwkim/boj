N = int(input())
nums = [0] + [*map(int, input().split())]
for i in range(1, N + 1):
    nums[i] += nums[i-1]
ans = 1e9
for i in range(N + 1):
    ans = min(ans, nums[N] + i - 2 * nums[i])
print(ans)