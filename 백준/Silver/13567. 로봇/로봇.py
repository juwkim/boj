dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y, d = 0, 0, 0
M, N = map(int, input().split())
for _ in range(N):
    cmd, num = input().split()
    num = int(num)
    if cmd == 'MOVE':
        x += dx[d] * num
        y += dy[d] * num
        if not (0 <= x <= M and 0 <= y <= M):
            x = -1
            break
    else:
        d = (d + num - (num == 0)) % 4

if x == -1:
    print(-1)
else:
    print(x, y)