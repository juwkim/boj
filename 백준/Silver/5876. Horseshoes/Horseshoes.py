def solve(i, j, opens, closes, visited, phase):
    global max_k
    if phase and opens == closes:
        max_k = max(max_k, opens)
        return
    for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
        if 0 <= ni < N and 0 <= nj < N and not visited & (1 << ni * N + nj):
            c = grid[ni][nj]
            if phase:
                if c == ')' and closes < opens:
                    solve(ni, nj, opens, closes + 1, visited | (1 << ni * N + nj), 1)
            elif c == '(':
                solve(ni, nj, opens + 1, closes, visited | (1 << ni * N + nj), 0)
            elif c == ')' and opens > closes:
                solve(ni, nj, opens, closes + 1, visited | (1 << ni * N + nj), 1)
N = int(input())
grid = [input() for _ in range(N)]
max_k = 0
if grid[0][0] == '(':
    solve(0, 0, 1, 0, 1, 0)
print(max_k * 2)