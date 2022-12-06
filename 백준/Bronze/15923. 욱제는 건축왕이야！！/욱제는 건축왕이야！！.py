N = int(input())
points = [input().split() for _ in range(N)]
x_points, y_points = [int(x[0]) for x in points], [int(y[1]) for y in points]
print(2 * (max(x_points) + max(y_points) - min(x_points) - min(y_points)))