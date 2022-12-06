g = lambda: [*map(int, input().split())]
while int(input()):
    nums = g()
    new = [0] * len(nums)
    for i in range(len(nums)):
        new[nums[i] - 1] = i + 1
    if nums == new:
        print('ambiguous')
    else:
        print('not ambiguous')