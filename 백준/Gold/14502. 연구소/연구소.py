def dfs(x, y):
    global num
    for p, q in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
        if 0 <= p < N and 0 <= q < M and board[p][q] == 0:
            board[p][q] = 2
            num += 1
            dfs(p, q)

from itertools import combinations
from copy import deepcopy
g = lambda: [*map(int, input().split())]
N, M = g()
Map = [g() for _ in range(N)]

zero = -3
zero_idxes = []
for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            zero += 1
            zero_idxes.append((i, j))
Min = 100
for a, b, c in combinations(zero_idxes, 3):
    board = deepcopy(Map)
    board[a[0]][a[1]] = 1
    board[b[0]][b[1]] = 1
    board[c[0]][c[1]] = 1
    num = 0    
    for x in range(N):
        for y in range(M):
            if board[x][y] == 2:
                for p, q in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0 <= p < N and 0 <= q < M and board[p][q] == 0:
                        board[p][q] = 2
                        num += 1
                        dfs(p, q)
    Min = min(Min, num)
print(zero - Min)