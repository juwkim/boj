n, d, k = map(int, input().split())
log = {(0, 0)}
x, y, direc = 0, 0, 0
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
min_x, min_y, max_x, max_y = 0, 0, 0, 0
cnt, prvcnt, check = d, d, 1
for _ in range(n):
    cnt -= 1
    x, y = x + dx[direc], y + dy[direc]
    min_x, min_y, max_x, max_y = min(min_x, x), min(min_y, y), max(max_x, x), max(max_y, y)
    log.add((x, y))
    if cnt == 0:
        direc = (direc + 1) % 4
        check ^= 1
        if check:
            prvcnt *= k
        cnt = prvcnt
print(max_y - min_y + 1, max_x - min_x + 1)
for i in range(min_y, max_y + 1):
    for j in range(min_x, max_x + 1):
        print(".*"[(j, i) in log], end="")
    print()