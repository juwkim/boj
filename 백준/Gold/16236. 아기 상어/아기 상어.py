from collections import deque

N = int(input())
board = []
x, y = 0, 0
for i in range(N):
    board.append(l:=[*map(int, input().split())])
    if 9 in l:
        x, y = i, l.index(9)
        board[x][y] = 0

s, ate, cnt = 2, 0, 0
dq = deque([(x, y, cnt)])
visited = [bytearray(N) for _ in range(N)]
pts = -1, -1
while True:
    while dq:
        x, y, t = dq.popleft()
        visited[x][y] = 1
        for a, b in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
            if 0 <= a < N and 0 <= b < N and not visited[a][b] and board[a][b] <= s:
                visited[a][b] = 1
                if 0 < board[a][b] < s:
                    if pts == (-1, -1):
                        pts, cnt = (a, b), t + 1
                    elif cnt == t + 1:
                        if (a, b) < pts: pts = (a, b)
                    else:
                        break
                else:
                    dq.append((a, b, t + 1))

    if pts == (-1, -1): break
    a, b = pts
    dq = deque([(a, b, cnt)])
    visited = [bytearray(N) for _ in range(N)]
    board[a][b] = 0
    ate += 1
    if ate == s:
        s += 1
        ate = 0
    pts = -1, -1
print(cnt)