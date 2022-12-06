def check(m):
    cnt = 0
    
    cur = 0
    for num in nums:
        if num > m:
            return False
        cur += num
        if cur > m:
            cnt += 1
            cur = num
    if cur:
        cnt += 1
    return cnt <= M

g = lambda: [*map(int, input().split())]

N, M = g()
nums = g()
lo, hi = 0, sum(nums)
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)