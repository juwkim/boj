import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from math import pi

for tc in range(1, 1 + int(input())):
    N, K = g()
    nums = []
    for _ in range(N):
        R, H = g()
        nums.append((R * H, R * R))
    nums.sort(reverse=True)
    ans = 2 * sum(nums[i][0] for i in range(K - 1))
    s = max(nums[i][1] for i in range(K)) + 2 * nums[K - 1][0]
    for i in range(K, N):
        s = max(s, nums[i][1] + 2 * nums[i][0])
    ans += s
    print(f"Case #{tc}: {ans * pi}")