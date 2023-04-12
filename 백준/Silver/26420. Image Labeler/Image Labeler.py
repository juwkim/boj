g = lambda: [*map(int, input().split())]

for case in range(1, 1 + int(input())):
    N, M = g()
    nums = sorted(g())
    
    a, b = nums[:N-M+1], nums[N-M+1:]
    
    t = len(a)
    if t & 1:
        ans = a[t // 2]
    else:
        ans = (a[t // 2 - 1] + a[t // 2]) / 2
    ans += sum(b)
    
    print(f'Case #{case}: {ans}')