import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

w, h, n = g()
x_list, y_list = [0, w + 1], [0, h + 1]
for _ in range(n):
    x, y = g()
    x_list.append(x)
    y_list.append(y)
x_list.sort()
y_list.sort()
p = max(b - a for a, b in zip(x_list, x_list[1:])) - 1
q = max(b - a for a, b in zip(y_list, y_list[1:])) - 1
print(p * q)