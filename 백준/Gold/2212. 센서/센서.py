N, K, *nums = map(int, open(0).read().split())
nums.sort()
print(sum(sorted(nums[i + 1] - nums[i] for i in range(N - 1))[:max(0, N - K)]))