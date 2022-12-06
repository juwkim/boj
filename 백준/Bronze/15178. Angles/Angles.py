for _ in range(int(input())):
    nums = [*map(int, input().split())]
    print(*nums, ['Check', 'Seems OK'][sum(nums) == 180])