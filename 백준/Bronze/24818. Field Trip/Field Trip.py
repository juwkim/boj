from bisect import *
g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
for i in range(1, n):
    nums[i] += nums[i-1]

if nums[-1] % 3:
    print(-1)
else:
    p = nums[-1] // 3
    s, i = bisect_right(nums, p), bisect_left(nums, p)
    t, j = bisect_right(nums, 2 * p), bisect_left(nums, 2 * p)
    if s - i == 1 and t - j == 1:
        print(i + 1, j + 1)
    else:
        print(-1)