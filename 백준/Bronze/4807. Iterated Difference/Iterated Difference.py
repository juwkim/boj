i = 1
while (n:= input()) != '0':
    nums = [*map(int, input().split())]
    cnt = 0
    while len(set(nums)) != 1 and cnt < 1000:
        cnt += 1
        nums = [abs(b - a) for a, b in zip(nums, nums[1:] + [nums[0]])]

    if len(set(nums)) != 1:
        print(f'Case {i}: not attained')
    else:
        print(f'Case {i}: {cnt} iterations')
    i += 1