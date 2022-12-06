g = lambda: [*map(int, input().split())]
N, M = g()
r, c, d = g()
Map = [g() for _ in range(N)]
dr = [-1, 0, 1, 0]  # 북, 동, 남, 서
dc = [0, 1, 0, -1]

def get_direction(r, c, d):
    for i in range(d + 3, d - 1, -1):
        next_d = i % 4
        nr, nc = r + dr[next_d], c + dc[next_d]
        if Map[nr][nc] == 0:
            return nr, nc, next_d
    next_d = (d + 2) % 4
    nr, nc = r + dr[next_d], c + dc[next_d]
    if Map[nr][nc] == 1:
        return -1, -1, -1
    else:
        return nr, nc, d

def solve(r, c, d):

    ans = 0
    while True:
        if Map[r][c] == 0:
            Map[r][c] = 2
            ans += 1
        r, c, d = get_direction(r, c, d)
        if r == -1:
            return ans
print(solve(r, c, d))