import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
Sum = sum(nums)
ans = None
for idx, num in enumerate(sorted(nums, reverse=True)):
    if num * (N - idx) <= Sum:
        ans = idx
        break
print(ans)