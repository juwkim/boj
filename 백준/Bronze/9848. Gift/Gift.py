n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
print(sum(nums[i] - nums[i+1] >= k for i in range(n-1)))