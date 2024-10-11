A = [[c for c in input()] for _ in range(12)]
ans = 0
while True:
    puyo = []
    visited = [bytearray(6) for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if visited[i][j] or A[i][j] == ".":
                continue
            visited[i][j] = True
            st = [(i, j)]
            tmp = [(i, j)]
            c = A[i][j]
            while st:
                x, y = st.pop()
                for nx, ny in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and A[nx][ny] == c:
                        visited[nx][ny] = True
                        st.append((nx, ny))
                        tmp.append((nx, ny))
            if len(tmp) >= 4:
                puyo.extend(tmp)
    if not puyo:
        break
    ans += 1
    for x, y in puyo:
        A[x][y] = "."
    for j in range(6):
        i = 11
        for k in range(11, -1, -1):
            if A[k][j] != '.':
                A[i][j] = A[k][j]
                i -= 1
        for k in range(i, -1, -1):
            A[k][j] = "."
print(ans)