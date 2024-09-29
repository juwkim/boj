N, *nums = map(int, open(0).read().split())
nums.sort()
ans = 0
for i, num in enumerate(nums):
    l, r = 0, N - 1
    if l == i:
        l += 1
    if r == i:
        r -= 1
    while l < r:
        s = nums[l] + nums[r]
        if s == num:
            ans += 1
            break
        if s < num:
            l += 1
            if l == i:
                l += 1
        else:
            r -= 1
            if r == i:
                r -= 1
print(ans)