import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

h, w = g()
nums = [g() for _ in range(h)]
for i in range(1, h):
    nums[i][0] += max(nums[i-1][:2])
    for j in range(1, w):
        nums[i][j] += max(nums[i-1][j-1:j+2])
print(max(nums[-1]))