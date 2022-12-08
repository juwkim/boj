g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    N = int(input())
    check = set()
    nums = g()
    while True:
        if sum(nums) == 0:
            ans = 'ZERO'
            break
        l = tuple(nums)
        if l in check:
            ans = 'LOOP'
            break
        check.add(l)
        
        tmp = []
        for a, b in zip(nums, nums[1:]):
            tmp.append(abs(a - b))
        tmp.append(abs(nums[0] - nums[-1]))
        nums = tmp        
    print(ans)