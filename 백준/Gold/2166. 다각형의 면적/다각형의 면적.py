N = int(input())
points = [[*map(int, input().split())] for _ in range(N)]
x0, y0 = points[0]
points = [[x - x0, y - y0] for x, y in points]
ans = sum(points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1] for i in range(1, N-1))
print(f'{abs(ans)/2:.1f}')