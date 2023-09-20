import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, m, S = g()
nums = [g() for _ in range(n)]
ans = 0
for size in range(1, min(n, m) + 1):
    for i in range(n + 1 - size):
        for j in range(m + 1 - size):
            harvest = sum(sum(nums[k][j:j+size]) for k in range(i, i + size))
            ans += harvest < S
print(ans)