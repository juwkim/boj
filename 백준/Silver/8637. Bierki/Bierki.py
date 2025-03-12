N, *nums = map(int, open(0))
nums.sort()
ans = 3
l, r = 0, 2
while r < N:
    if nums[r] < nums[l] + nums[l + 1]:
        r += 1
        ans = max(ans, r - l)
    else:
        l += 1
print(ans)