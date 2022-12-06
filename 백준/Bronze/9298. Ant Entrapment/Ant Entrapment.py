import sys
for i in range(1, 1 + int(input())):
    N = int(input())
    ant = [[*map(float, sys.stdin.readline().split())] for _ in range(N)]
    x, y = map(sorted, zip(*ant))
    area = (x[-1] - x[0]) * (y[-1] - y[0])
    perimeter = 2 * (x[-1] - x[0] + y[-1] - y[0])
    print(f'Case {i}: Area {area}, Perimeter {perimeter}')