g = lambda: [*map(int, input().split())]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y, d = 0, 0, 0
N, T = g()
prev = 0
for _ in range(N):
    ti, si = input().split()
    ti = int(ti)
    x += dx[d] * (ti - prev)
    y += dy[d] * (ti - prev)
    prev = ti
    if si == 'right':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4    
    
x += dx[d] * (T - prev)
y += dy[d] * (T - prev)
print(x, y)