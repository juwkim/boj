import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

N, U = g()
grid = [[c == '#' for c in input()] for _ in range(N)]
cnt = [[0] * (N >> 1) for _ in range(N >> 1)]
for i in range(N):
    x = min(i, N - i - 1)
    for j, c in enumerate(grid[i]):
        y = min(j, N - j - 1)
        cnt[x][y] += c
print(ans:=sum(min(x, 4 - x) for row in cnt for x in row))
for _ in range(U):
    i, j = map(lambda x: int(x) - 1, input().split())
    x, y = min(i, N - i - 1), min(j, N - j - 1)
    grid[i][j] ^= 1
    p = min(cnt[x][y], 4 - cnt[x][y])
    if grid[i][j]:
        cnt[x][y] += 1
    else:
        cnt[x][y] -= 1
    ans += min(cnt[x][y], 4 - cnt[x][y]) - p
    print(ans)