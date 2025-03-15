import sys
input = sys.stdin.readline

N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
idx = max(range(N), key=lambda x: nums[x][1])
x, y = nums[idx]
xl, yl = nums[idx - 1]
xll, yll = nums[idx - 1]
for i in range(idx - 2, -1, -1):
    x1, y1 = nums[i]
    if (xll - x) * (y1 - y) <= (x1 - x) * (yll - y):
        xll, yll = x1, y1
        if y1 <= yl:
            xl, yl = x1, y1
xr, yr = nums[idx + 1]
xrr, yrr = nums[idx + 1]
for i in range(idx + 2, N):
    x1, y1 = nums[i]
    if (xrr - x) * (y1 - y) >= (x1 - x) * (yrr - y):
        xrr, yrr = x1, y1
        if y1 <= yr:
            xr, yr = x1, y1
print(xl, yl)
print(xr, yr)