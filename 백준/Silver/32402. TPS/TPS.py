import sys
input = lambda: sys.stdin.readline().rstrip()

dx = 0, 1, 0, -1
dy = 1, 0, -1, 0
x, y, d = 0, 0, 0
for _ in range(int(input())):
    s = input()
    if s == "MR":
        d = (d + 1) % 4
    elif s == "ML":
        d = (d - 1) % 4
    else:
        i = d - "WASD".index(s)
        x += dx[i]
        y += dy[i]
    print(x, y, x + dx[d - 2], y + dy[d - 2])