import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
for i in range(1, n):
    nums[i] *= 1 + nums[i - 1] // nums[i]
print(*nums)