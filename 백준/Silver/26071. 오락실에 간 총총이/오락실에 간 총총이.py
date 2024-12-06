import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
x_min, x_max, y_min, y_max = N, -1, N, -1
for i in range(N):
    for j, c in enumerate(input()):
        if c == 'G':
            x_min, x_max, y_min, y_max = min(x_min, i), max(x_max, i), min(y_min, j), max(y_max, j)
if x_min == x_max and y_min == y_max:
    print(0)
elif x_min == x_max:
    print(min(y_max, N - 1 - y_min))
elif y_min == y_max:
    print(min(x_max, N - 1 - x_min))
else:
    print(min(x_max, N - 1 - x_min) + min(y_max, N - 1 - y_min))