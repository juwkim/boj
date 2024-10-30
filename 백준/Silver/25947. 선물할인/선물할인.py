n, b, a, *nums = map(int, open(0).read().split())
nums.sort()
ans, cur = n, 0
for i in range(n):
    cur += nums[i] >> 1
    if i >= a:
        cur += nums[i - a] >> 1
    if cur > b:
        ans = i
        break
print(ans)