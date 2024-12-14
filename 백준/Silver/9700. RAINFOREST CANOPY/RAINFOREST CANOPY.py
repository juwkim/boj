import sys
input = sys.stdin.readline

tc = 1
while True:
    try:
        N = int(input())
        a = [input() for _ in range(N)]
        visited = [bytearray(N) for _ in range(N)]
        ans = 0
        for i in range(N):
            for j in range(N):
                if a[i][j] == '0' or visited[i][j]:
                    continue
                ans += 1
                visited[i][j] = 1
                st = [(i, j)]
                while st:
                    x, y = st.pop()
                    for nx, ny in (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1):
                        if 0 <= nx < N and 0 <= ny < N and a[nx][ny] == '1' and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            st.append((nx, ny))
        print(f"Case #{tc}: {ans}")
        tc += 1
    except:
        break