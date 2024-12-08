import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
a = [input() for _ in range(N)]
p, max = 0, 0
for y in range(N):
    for x in range(N):
        if a[y][x] != '.':
            continue
        cnt = 0
        for dy, dx in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            cur, good = 0, False
            ny, nx = y + dy, x + dx
            while 0 <= ny < N and 0 <= nx < N:
                if a[ny][nx] == 'B':
                    good = True
                    break
                elif a[ny][nx] == '.':
                    break
                cur += 1
                ny += dy
                nx += dx
            if good:
                cnt += cur
        if cnt > max:
            p, max = (x, y), cnt
if max:
    print(*p)
    print(max)
else:
    print("PASS")