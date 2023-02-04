n, m, a, c, x = map(int, input().split())

nums = []
for i in range(n):
    x = (a * x + c) % m
    nums.append(x)

ans = 0
for num in nums:
    l, r = 0, n - 1
    while l < r + 1:
        m = (l + r) // 2
        if nums[m] == num:
            ans += 1
            break
        elif nums[m] > num:
            r = m - 1
        else:
            l = m + 1
print(ans)