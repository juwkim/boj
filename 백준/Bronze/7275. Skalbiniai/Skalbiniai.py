import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K, M = g()
buf = [g()[1:] for _ in range(K)]
nums = [0] + g()
ans = 0
for l in buf:
    cnt = sum(nums[i] for i in l)
    ans += (cnt + M - 1) // M
print(ans)