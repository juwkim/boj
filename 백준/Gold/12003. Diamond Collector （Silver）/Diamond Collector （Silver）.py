import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

from bisect import bisect_right
N, K = g()
nums = sorted(int(input()) for _ in range(N))

# p[i] = the number of p[i] ~ p[i] + K in nums
p = [bisect_right(nums, nums[i] + K, i+1) - i for i in range(N)]

# pmax[i] = max(p[i:])
pmax = [0] * (N - 1) + [p[-1]]
for i in range(N-2, -1, -1):
    pmax[i] = max(pmax[i+1], p[i])

idx = 0
ans = 0
while idx + p[idx] < N:
    ans = max(ans, p[idx] + pmax[idx + p[idx]])
    idx += 1
print(ans)