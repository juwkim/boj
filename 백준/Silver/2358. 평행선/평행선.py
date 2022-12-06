import sys
from math import comb
input = sys.stdin.readline
x_points, y_points = {}, {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    try:
        x_points[x] += 1
    except:
        x_points[x] = 1
    
    try:
        y_points[y] += 1
    except:
        y_points[y] = 1

x_lines = sum(num > 1 for num in y_points.values())
y_lines = sum(num > 1 for num in x_points.values())
print(x_lines + y_lines)