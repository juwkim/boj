import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

R, C = g()
a = [[*map(int, input())] for _ in range(R)]
Y, X, K = g()
color = a[Y][X]
if color != K:
    a[Y][X] = K
    st = [(Y, X)]
    while st:
        y, x = st.pop()
        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and a[ny][nx] == color:
                a[ny][nx] = K
                st.append((ny, nx))
for l in a:
    print(*l, sep='')