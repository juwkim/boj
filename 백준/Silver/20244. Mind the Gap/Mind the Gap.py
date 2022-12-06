n = int(input())
nums = [0] + sorted(map(int, input().split()))
ans = 0
for i in range(n):
    ans = max(ans, nums[i+1] - nums[i])
for i in range(n-1):
    if ans >= nums[i+2] - nums[i]:
        ans = 0
        break
print(ans)