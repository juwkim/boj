import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans = 2 * (N + sum(nums)) + nums[0] + nums[-1]
for i in range(N - 1):
    ans += abs(nums[i] - nums[i + 1])
print(ans)