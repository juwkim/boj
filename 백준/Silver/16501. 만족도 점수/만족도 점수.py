from itertools import combinations

ans = 0
a0, *nums = map(int, input().split())
for s in combinations(range(7), 3):
    total1 = sum(nums[a] for a in s)
    for a1 in s:
        cur1 = 1 - abs(a0 + 2 * nums[a1] - total1) / 20
        i, *t = {*range(7)} - {*s}
        b0 = nums[i]
        total2 = sum(nums[b] for b in t)
        for b1 in t:
            cur2 = 1 - abs(b0 + 2 * nums[b1] - total2) / 20
            ans = max(ans, min(cur1, cur2))
print(ans)