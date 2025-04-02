import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

ans, cur = 0, 0
prev_direc = 0
N = int(input())
x1, y1 = g()
for i in range(N - 1):
    x2, y2 = g()
    if x2 <= x1:
        cur, prev_direc = 0, 0
    else:
        direction = (0, 1, 2)[(y2 > y1) - (y2 < y1)]
        if direction:
            if prev_direc == 0 or prev_direc + direction != 3:
                cur = 1
            else:
                cur += 1
        prev_direc = direction
        ans = max(ans, cur)
    x1, y1 = x2, y2

print((ans, "EI OLE")[ans < 2])