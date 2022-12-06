g = lambda: [*map(int, input().split())]

nums = []
for _ in range(4):
    a, b = g()
    nums.append(b - a)
for i in range(3, 1, -1):
    nums[i-1] += nums[i]
for i in range(1, 4):
    print(nums[i])