for _ in range(int(input())):
    nums = [*map(int, input().split())]
    for i in range(18, -1, -1):
        nums[i] += nums[i+1] // 2
        nums[i+1] %= 2
    print(*nums)