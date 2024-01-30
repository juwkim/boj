import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = [*map(int, input().split())]
a = [0] * (n + 1)
for i, num in enumerate(nums):
    a[i + 1] = a[i] + 1 - num
b = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    b[i] = b[i + 1] + nums[i]
ans = min(s + t for s, t in zip(a, b))
print(ans)