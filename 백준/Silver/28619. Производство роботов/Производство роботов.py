n, *a = map(int, open(0).read().split())
t = 0
nums = []
for i, num in enumerate(a, 1):
    q, r = divmod(num, 100)
    t += q
    if r:
        nums.append((r, i))
nums.sort()
l, r = 0, len(nums) - 1
ans = []
while l < r:
    s = nums[l][0] + nums[r][0]
    if s >= 100:
        ans.append((nums[l][1], nums[r][1]))
        t += 1
        r -= 1
    l += 1
print(t)
print(len(ans))
for a, b in ans:
    print(a, b)