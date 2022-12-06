g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    N, *nums = g()
    nums.sort()
    Min = nums[0]
    Max = nums[-1]
    gap = max(j - i for i, j in zip(nums, nums[1:]))
    print('Class', _)
    print(f'Max {Max}, Min {Min}, Largest gap {gap}')