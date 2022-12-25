N, *nums = map(int, open(0))
ans = 0
def solve(l, r):
    global ans
    m = (l + r) >> 1
    if r - l > 1:
        solve(l, m)
        solve(m + 1, r)
    if nums[l] > nums[m + 1]:
        for i, j in zip(range(l, m + 1), range(m + 1, r + 1)):
            nums[i], nums[j] = nums[j], nums[i]
        ans += (m + 1 - l) ** 2 * 2
solve(0, len(nums) - 1)
print(ans)
for num in nums:
    print(num)