from bisect import bisect

N, T, *a = map(int, open(0).read().split())
nums = []
for i in range(1, int(T**.5) + 1):
    q, r = divmod(T, i)
    if r == 0:
        nums.append(i)
        if i != q:
            nums.append(q)
nums.sort()
nums.append(1e9)
ans = 0
for num in a:
    idx = bisect(nums, num)
    ans += min(num - nums[idx - 1], nums[idx] - num)
print(ans)