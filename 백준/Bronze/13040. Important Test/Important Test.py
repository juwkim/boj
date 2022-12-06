g = lambda: [*map(int, input().split())]

n, t, t0 = g()
for _ in range(n):
    m, *nums = g()
    
    tmp, idx = 0, 0
    while idx < m and tmp < t:
        tmp += nums[idx]
        idx += 1
    
    ans = 0
    i = 0
    while i < idx:
        l = nums.copy()
        l[i] = t0
        total, j = 0, 0
        while True:
            total += l[j]
            j += 1
            if total == t:
                res = j
                break
            elif total > t:
                res = j - 1
                break
            if j == m:
                res = j
                break
        ans = max(ans, res)
        if ans == n:
            break
        i += 1
    print(ans)