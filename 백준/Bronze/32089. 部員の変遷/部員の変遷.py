while n:=int(input()):
    nums = [*map(int, input().split())]
    cur = sum(nums[:3])
    ans = cur
    for i in range(3, n):
        cur += nums[i] - nums[i - 3]
        ans = max(ans, cur)
    print(ans)