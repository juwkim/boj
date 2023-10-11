import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = [0] * (100_003)
for _ in range(N):
    a, b = g()
    nums[a] += 1
    nums[b + 1] -= 1

ans, cur = 0, 0
for i in range(2, 100_002):
    cur += nums[i]
    if cur >= i - 1:
        ans = i - 1
print(ans)