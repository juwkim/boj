input = __import__('sys').stdin.readline

from collections import deque, defaultdict
def g(): return [*map(int, input().split())]

N, M = g()
board = [g() for _ in range(N)]
cheese = sum(sum(line) for line in board)

ans = 0
while cheese:
    ans += 1
    melted = defaultdict(int)
    dq = deque([(0, 0)])
    visited = [bytearray(M) for _ in range(N)]
    visited[0][0] = 1
    while dq:
        i, j = dq.popleft()
        for p, q in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= p < N and 0 <= q < M and visited[p][q] == 0:
                if board[p][q]:
                    melted[(p, q)] += 1
                else:
                    visited[p][q] = 1
                    dq.append((p, q))

    for x, y in melted:
        if melted[(x, y)] >= 2:
            cheese -= 1
            board[x][y] = 0
print(ans)