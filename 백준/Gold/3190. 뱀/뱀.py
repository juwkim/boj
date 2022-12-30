from collections import deque
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

change = {}
for _ in range(int(input())):
    X, C = input().split()
    change[int(X)] = (C == 'L') - (C == 'D')

di, time = 0, 0
dq = deque([(0, 0)])
while True:
    if time in change:
        di = (di + change[time]) % 4
    time += 1
    x, y = dq[0][0] + dx[di], dq[0][1] + dy[di]
    if 0 <= x < N and 0 <= y < N and (x, y) not in dq:
        dq.appendleft((x, y))
        if board[x][y] == 0:
            dq.pop()
        board[x][y] = 0
    else:
        break
print(time)