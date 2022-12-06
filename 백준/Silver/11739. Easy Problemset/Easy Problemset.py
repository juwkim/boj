g = lambda: [*map(int, input().split())]

n, k = g()
nums = [g() for _ in range(n)]
max_len = max(map(len, nums))
for i in range(n):
    if len(nums[i]) < max_len:
        nums[i] += [50] * (max_len - len(nums[i]))
nums = sum([list(l) for l in zip(*nums)][1:], [])

ans = 0
for i in range(len(nums)):
    if nums[i] >= ans:
        ans += nums[i]
        prev = nums[i]
        nums[i] -= 0.5
        k -= 1
        if k == 0:
            break

if k == 0:
    print(ans)
else:
    print(ans + k * 50)