import sys
input = sys.stdin.readline

n = int(input())
x, y = zip(*[[*map(int, input().split())] for _ in range(n)])
min_x, min_y = min(x), min(y)
if [i for i in range(n) if x[i] == min_x] == [i for i in range(n) if y[i] == min_y]:
    print(min_x, max(y))
else:
    print(min_x, min_y)