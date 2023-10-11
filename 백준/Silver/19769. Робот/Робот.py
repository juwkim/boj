import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
nums = sorted(g())
s = sum(nums)
ans = max(abs(s - 2 * sum(i for i in nums[:k] if i < 0)), abs(s - 2 * sum(i for i in nums[-k:] if i > 0)))
print(ans)