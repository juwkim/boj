import sys
input = sys.stdin.readline

ans = -1
a = [[-1] * 20 for _ in range(20)]
for i in range(1, int(input()) + 1):
    x, y = map(int, input().split())
    cur = i & 1
    a[x][y] = cur
    for dx, dy in (0, 1), (1, 0), (1, 1), (1, -1):
        cnt = 1
        for j in range(1, 6):
            nx, ny = x + dx * j, y + dy * j
            if not (1 <= nx <= 19 and 1 <= ny <= 19 and a[nx][ny] == cur):
                break
            cnt += 1
        for j in range(1, 6):
            nx, ny = x - dx * j, y - dy * j
            if not (1 <= nx <= 19 and 1 <= ny <= 19 and a[nx][ny] == cur):
                break
            cnt += 1
        if cnt == 5:
            ans = i
            break
    if ans != -1:
        break
print(ans)