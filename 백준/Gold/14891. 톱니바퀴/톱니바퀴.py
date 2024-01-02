import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

gears = [deque(input()) for _ in range(4)]
for _ in range(int(input())):
    idx, d = g()
    idx -= 1
    dirs = [0] * 4
    dirs[idx] = d
    for i in range(idx, 3):
        if gears[i][2] != gears[i + 1][6]:
            dirs[i + 1] = -dirs[i]
    for i in range(idx, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            dirs[i - 1] = -dirs[i]
    for gear, d in zip(gears, dirs):
        gear.rotate(d)
ans = 0
for i, gear in enumerate(gears):
    if gear[0] == "1":
        ans += 2 ** i
print(ans)