import sys
input = lambda: sys.stdin.readline().rstrip()
from math import inf

board = [[0] * 2001 for _ in range(2001)]
x, y, t, ans = 1000, 1000, 1, inf
board[x][y] = 1
for _ in range(int(input())):
    D, S = input().split()
    dx = {"N": 0, "S": 0, "E": 1, "W": -1}[D]
    dy = {"N": 1, "S": -1, "E": 0, "W": 0}[D]
    for _ in range(int(S)):
        x += dx
        y += dy
        t += 1
        if board[x][y]:
            ans = min(ans, t - board[x][y])
        board[x][y] = t
print(ans if ans != inf else -1)