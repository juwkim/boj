import sys
g = lambda: map(int, sys.stdin.readline().split())

dx = -1, 1, 0, 0
dy = 0, 0, -1, 1
R, C = g()
a = [bytearray(C) for _ in range(R)]
for _ in range(int(input())):
    br, bc = g()
    a[br][bc] = 1
sr, sc = g()
idx = 0
d = [num - 1 for num in g()]
while True:
    a[sr][sc] = 1
    for _ in range(4):
        nr = sr + dx[d[idx]]
        nc = sc + dy[d[idx]]
        if 0 <= nr < R and 0 <= nc < C and not a[nr][nc]:
            sr, sc = nr, nc
            break
        idx = (idx + 1) % 4
    else:
        break
print(sr, sc)