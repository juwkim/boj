N, K, M, *L = map(int, open(0).read().split())
nums = []
for num in L:
    if num <= K or num == 2 * K:
        continue
    if num < 2 * K:
        nums.append(num - K)
    else:
        nums.append(num - 2 * K)
if sum(nums) < M:
    print(-1)
else:
    lo, hi = 1, max(nums) + 1
    while hi > lo + 1:
        mid = (lo + hi) // 2
        if sum(num // mid for num in nums) < M:
            hi = mid
        else:
            lo = mid
    print(lo)