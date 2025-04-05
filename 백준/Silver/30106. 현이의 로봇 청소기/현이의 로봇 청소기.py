import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M, K = g()
nums = [g() for _ in range(N)]
ans = 0
visited = [bytearray(M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        visited[i][j] = 1
        ans += 1
        st = [(i, j)]
        while st:
            x, y = st.pop()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and abs(nums[nx][ny] - nums[x][y]) <= K:
                    visited[nx][ny] = 1
                    st.append((nx, ny))
print(ans)