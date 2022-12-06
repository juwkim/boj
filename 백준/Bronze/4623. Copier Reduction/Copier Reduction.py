while True:
    nums = [*map(int, input().split())]
    if nums == [0, 0, 0, 0]:
        break
    A, B = sorted(nums[:2])
    C, D = sorted(nums[2:])
    print(f'{int(100/max(A/C, B/D, 1))}%')