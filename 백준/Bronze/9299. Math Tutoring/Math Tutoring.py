for j in range(int(input())):
    nums = [*map(int, input().split())]
    derivative = [nums[nums[0]-i+1]*i for i in range(nums[0], 0, -1)]
    print(f'Case {j+1}: {nums[0]-1}', *derivative)