import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
dist = []
for _ in range(N):
    P = int(input())
    nums = g()
    dist.append(max(nums[i] ** 2 + nums[i + 1] ** 2 for i in range(0, 2 * P, 2)))
ans = sorted(dist)[K - 1]
print(f"{ans:.2f}")