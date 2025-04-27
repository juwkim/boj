import sys
import math
input = sys.stdin.readline

n = int(input())
xs, ys = zip(*[[*map(int, input().split())] for _ in range(n)])
ans = 0
for i in range(1, n - 1):
    ans = max(ans, math.atan(ys[i] / (xs[i] - xs[0])), math.atan(ys[i] / (xs[-1] - xs[i])))
print(math.degrees(ans))