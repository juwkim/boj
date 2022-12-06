g = lambda: [*map(int, input().split())]

n, k = g()
nums = g()
ans = 0
while nums != sorted(nums):
    for i in range(n + 1 - k):
        nums[i:i+k] = sorted(nums[i:i+k])
    ans += 1
print(ans)