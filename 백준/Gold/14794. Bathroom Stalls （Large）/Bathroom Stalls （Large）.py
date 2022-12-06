for i in range(1, 1+int(input())):
    N, K = map(int, input().split())
    odd, even = N%2, 1 - N%2
    nums, d = set([N]), 0
    while 2**(d+1) <= K:
        d += 1

    for _ in range(d):
        count_odd, count_even, now = 0, 0, set()
        
        for _ in range(len(nums)):
            a, b = divmod(nums.pop(), 2)
            if b:
                now.update([a])
                count_odd, count_even = count_odd + a%2*2*odd, count_even + (1-a%2)*2*odd 
            else:
                if a > 1:
                    now.update([a-1, a])
                    count_even += even
                else:
                    now.update([a])
                count_odd += even
                
        odd, even, nums = count_odd, count_even, now
    if (max(nums)%2 and K < 2**d + odd) or (max(nums)%2 == 0 and K < 2**d + even):
        t = max(nums)
    else:
        t = min(nums)
    print(f'Case #{i}: {t//2} {(t-1)//2}')