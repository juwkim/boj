g = lambda: [*map(int, input().split())]

from bisect import bisect_right
N, Q = g()
nums = g()
for i in range(1, N):
    nums[i] += nums[i - 1]

for num in g():
    idx = bisect_right(nums, num)
    if idx == N:
        print(-1)
    else:
        print(idx + 1)