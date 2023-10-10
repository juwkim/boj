import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
nums = [0] + sorted(g(), reverse=True)
ans = sum(nums[i] for i in range(1, n + 1) if i % k)
print(ans)