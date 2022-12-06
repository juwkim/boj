for _ in range(int(input())):
    N, X, Y = map(int, input().split())
    nums = [*map(int, input().split())]
    if nums[0] == X:
        if nums[-1] == Y:
            print('BOTH')
        else:
            print('EASY')
    else:
        if nums[-1] == Y:
            print('HARD')
        else:
            print('OKAY')