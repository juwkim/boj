import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    H, W = g()
    a = [g() for _ in range(H)]
    ans = [[''] * W for _ in range(H)]
    num = ord('a')
    for i in range(H):
        for j in range(W):
            if ans[i][j]:
                continue
            nc = chr(num)
            path = [(i, j)]
            while True:
                x, y = path[-1]
                l = [(nx, ny) for nx, ny in ((x-1, y), (x, y-1), (x, y+1), (x+1, y)) if 0 <= nx < H and 0 <= ny < W and a[nx][ny] < a[x][y]]
                if not l:
                    num += 1
                    break
                nx, ny = min(l, key=lambda x: a[x[0]][x[1]])
                if ans[nx][ny]:
                    nc = ans[nx][ny]
                    break
                path.append((nx, ny))
            for x, y in path:
                ans[x][y] = nc
    print(f'Case #{tc}:')
    for l in ans:
        print(*l)