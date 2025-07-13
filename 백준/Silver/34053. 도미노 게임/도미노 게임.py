import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
Min = 1e10
ans = 0
for _ in range(N):
    nums = g()
    ans += sum(nums)
    Min = min(Min, min(nums))
ans -= Min
print(ans)