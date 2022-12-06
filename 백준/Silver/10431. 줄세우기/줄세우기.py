g = lambda: [*map(int, input().split())]

from bisect import bisect_left
for _ in range(int(input())):
    T, *nums = g()
    ans = 0
    buf = []
    for i in range(len(nums)):
        idx = bisect_left(buf, nums[i])
        buf.insert(idx, nums[i])
        ans += i - idx
    print(T, ans)