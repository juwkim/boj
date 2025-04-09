import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    W, H = map(int, input().split())
    if W == 0:
        break
    S = [[*input()] for _ in range(H)]
    x, y = -1, -1
    for i in range(H):
        for j in range(W):
            if S[i][j] == '@':
                x, y = i, j
                break
        if x != -1:
            break
    S[x][y] = '#'
    st, cnt = [(x, y)], 1
    while st:
        x, y = st.pop()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
                S[nx][ny] = '#'
                cnt += 1
                st.append((nx, ny))
    print(cnt)