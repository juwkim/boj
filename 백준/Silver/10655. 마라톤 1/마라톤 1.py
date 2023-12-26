import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = [g() for _ in range(N)]
dist = []
for i in range(N - 1):
    x1, y1 = nums[i]
    x2, y2 = nums[i + 1]
    dist.append(abs(x1 - x2) + abs(y1 - y2))

gain = 0
for i in range(N - 2):
    gain = max(gain, dist[i] + dist[i + 1] - abs(nums[i][0] - nums[i + 2][0]) - abs(nums[i][1] - nums[i + 2][1]))
ans = sum(dist) - gain
print(ans)