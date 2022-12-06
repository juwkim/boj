while True:
    try:
        N = int(input())
        nums = [*map(int, input().split())]
        if N <= 2:
            print(1)
        else:
            idx = N - 1
            d = nums[-1] - nums[-2]
            while idx != 1 and nums[idx - 1] - nums[idx - 2] == d:
                    idx -= 1
            print(idx)
    except:
        break