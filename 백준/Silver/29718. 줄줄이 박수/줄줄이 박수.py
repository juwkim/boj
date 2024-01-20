import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
nums = g()
for _ in range(N - 1):
    for i, num in enumerate(g()):
        nums[i] += num
A = int(input())
cur = sum(nums[:A])
ans = cur
for i in range(A, M):
    cur += nums[i] - nums[i - A]
    ans = max(ans, cur)
print(ans)