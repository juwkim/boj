import sys
input = lambda: sys.stdin.readline().rstrip()

while N:=int(input()):
    board = [bytearray(21) for _ in range(21)]
    for _ in range(N):
        x, y = map(int, input().split())
        board[x][y] = 1
    x, y = 10, 10
    for _ in range(int(input())):
        d, l = input().split()
        dx = {"N": 0, "S": 0, "W": -1, "E": 1}[d]
        dy = {"N": 1, "S": -1, "W": 0, "E": 0}[d]
        for _ in range(int(l)):
            x += dx
            y += dy
            if board[x][y]:
                board[x][y] = 0
                N -= 1
    print("Yes" if N == 0 else "No")