import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
px = [0] * (N + 1)
for i in range(1, N + 1):
    px[i] = px[i - 1] + (i != N and nums[i - 1] > nums[i])
for _ in range(int(input())):
    x, y = g()
    print(px[y - 1] - px[x - 1])