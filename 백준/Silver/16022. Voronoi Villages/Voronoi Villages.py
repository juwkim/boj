n = int(input())
nums = sorted(int(input()) for _ in range(n))
ans = min(nums[i+2] - nums[i] for i in range(n-2)) / 2
print(f'{ans:.1f}')