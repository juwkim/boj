N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
cnt = [0, 0]
Sij1 = (0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)
Sij2 = (0, 0), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 1), (2, 2), (2, 4)

Cij1 = (0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2)
Cij2 = (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2)
Cij3 = (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 4)
Cij4 = (0, 0), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)

def match(i, j, l, w, h):
    if i + w > N or j + h > M:
        return False
    return all(grid[i + di][j + dj] == 'x' for di, dj in l)

def swap(i, j, l, idx):
    cnt[idx] += 1
    for di, dj in l:
        grid[i + di][j + dj] = '.'

def restore(i, j, l, idx):
    cnt[idx] -= 1
    for di, dj in l:
        grid[i + di][j + dj] = 'x'

def solve(step):
    if step == N * M:
        return all(grid[i][j] == '.' for i in range(N) for j in range(M))
    i, j = divmod(step, M)
    if grid[i][j] == '.':
        return solve(step + 1)
    else:
        for l, idx, w, h in (Sij1, 0, 5, 3), (Sij2, 0, 3, 5), (Cij1, 1, 5, 3), (Cij2, 1, 5, 3), (Cij3, 1, 3, 5), (Cij4, 1, 3, 5):
            if match(i, j, l, w, h):
                swap(i, j, l, idx)
                if solve(step + 1):
                    return True
                restore(i, j, l, idx)
solve(0)
print(*cnt)