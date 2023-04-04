while n := int(input()):
    nums = [*map(int, input().split())]
    h = nums[int(input()) - 1] + 1
    ans = sum(max(0, h - num) for num in nums)
    print(ans)