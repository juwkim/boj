import sys
input = sys.stdin.readline

x_min, x_max, y_max = 1e4, -1e4, 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if y:
        y_max = max(y_max, abs(y))
    else:
        x_min = min(x_min, x)
        x_max = max(x_max, x)
print(max(0, (x_max - x_min) * y_max / 2))