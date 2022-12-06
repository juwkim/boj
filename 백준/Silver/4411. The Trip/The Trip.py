while n:= int(input()):
    nums = []
    for _ in range(n):
        d, c = map(int, input().split('.'))
        nums.append(d * 100 + c)
    nums.sort(reverse=True)
    mean, remainder = divmod(sum(nums), n)
    
    ans = 0
    for i in range(n):
        ans += abs(mean - nums[i] + (i < remainder))
    
    r, q = divmod(ans // 2, 100)
    print(f'${r}.{q:02d}')