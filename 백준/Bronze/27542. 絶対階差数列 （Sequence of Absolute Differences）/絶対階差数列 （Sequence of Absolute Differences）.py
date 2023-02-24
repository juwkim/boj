N = int(input())
nums = [*map(int, input().split())]
for _ in range(N - 1):
    nums = [abs(a - b) for a, b in zip(nums, nums[1:])]
print(nums[0])