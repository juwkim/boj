import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans = (sum(nums) + max(nums)) / 2
print(ans)