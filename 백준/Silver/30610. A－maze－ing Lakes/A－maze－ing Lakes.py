import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [input() for _ in range(N)]
visited = [bytearray(M) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(M):
        if a[i][j] == '1' and not visited[i][j]:
            visited[i][j] = 1
            st, cnt = [(i, j)], 0
            while st:
                x, y = st.pop()
                cnt += 1
                for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
                    if 0 <= x < N and 0 <= y < M and a[nx][ny] == '1' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        st.append((nx, ny))
            ans.append(cnt)
print(len(ans))
print(*sorted(ans))