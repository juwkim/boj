import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dx = {"N": 1, "S": -1}
dy = {"E": 1, "W": -1}
for _ in range(int(input())):
    (r, c), (x, y), (t, s) = g(), g(), g()
    p, q = input()
    board = [[{('N', 'E'): False, ('N', 'W'): False, ('S', 'E'): False, ('S', 'W'): False} for _ in range(c + 1)] for _ in range(r + 1)]
    ans = "B cannot be reached from A."
    cnt = 0
    while True:
        if (x, y) == (t, s):
            ans = f"B can be reached from A after {cnt} move(s)."
            break
        if board[x][y][(p, q)] == True:
            break
        board[x][y][(p, q)] = True
        cnt += 1
        if x == r:
            p = "S"
        elif x == 0:
            p = "N"
        if y == c:
            q = "W"
        elif y == 0:
            q = "E"        
        x += dx[p]
        y += dy[q]
    print(ans)