n, k, *nums = map(int, open(0).read().split())
p = max((sum(nums) + k - 1) // k, *nums)
print(k * p - sum(nums))