import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

h = []
N, M = g()
for _ in range(N):
    nums = g()
    nums[nums.index(0)] = -sum(nums)
    tmp = []
    cur = 0
    for num in nums:
        cur += num
        tmp.append(cur)
    h.append(sum(tmp) / M)
ans = max(range(N), key=lambda x: h[x]) + 1
print(ans)