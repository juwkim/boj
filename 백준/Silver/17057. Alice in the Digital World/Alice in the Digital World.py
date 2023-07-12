g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n, m = g()
    nums = g()
    ans = 0    
    for i, num in enumerate(nums):
        if num != m:
            continue
        cur = m
        
        j = i + 1
        while j < n and nums[j] > m:
            cur += nums[j]
            j += 1
        j = i - 1
        while j >= 0 and nums[j] > m:
            cur += nums[j]
            j -= 1        
        ans = max(ans, cur)
    print(ans)