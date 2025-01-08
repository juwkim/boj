import sys
input = sys.stdin.readline

R, C, L = map(int, input().split())
a = [input() for _ in range(R)]
ans, s = 0, set()

def solve(x, y, cnt, path):
    global ans
    if cnt == L:
        ans += 1
        s.add("".join(path))
        return
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and a[nx][ny] not in "acm":
            solve(nx, ny, cnt + 1, path + [a[nx][ny]])

for i in range(R):
    for j in range(C):
        if a[i][j] in "acm":
            continue
        solve(i, j, 1, [a[i][j]])
print(ans)
print(len(s))