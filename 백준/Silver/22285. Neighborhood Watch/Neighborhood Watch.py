import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
nums = sorted(int(input()) for _ in range(K))
nums.append(N + 1)
ans = sum(a * (b - a) for a, b in zip(nums, nums[1:]))
print(ans)