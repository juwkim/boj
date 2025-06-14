import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
for _ in range(int(input())):
    H, W = g()
    path = input()
    grid = [g() for _ in range(H)]
    result = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            x, y = i, j
            total = grid[x][y]
            for move in path:
                x += dx[move]
                y += dy[move]
                if x < 0 or x >= H or y < 0 or y >= W:
                    break
                total += grid[x][y]
            else:
                result[i][j] = total
    for row in result:
        print(*row)