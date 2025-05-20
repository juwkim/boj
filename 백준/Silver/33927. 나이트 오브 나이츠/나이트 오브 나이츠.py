N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
visited = [bytearray(N) for _ in range(N)]
ans = 0
def solve(idx, total):
    global ans
    if idx == N * N:
        ans = max(ans, total)
        return
    solve(idx + 1, total)
    i, j = divmod(idx, N)
    if not visited[i][j]:
        check = [(i, j)]
        for di, dj in (1, -2), (1, 2), (2, -1), (2, 1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                check.append((ni, nj))
        visited[i][j] = 1
        solve(idx + 1, total + nums[i][j])
        for ni, nj in check:
            visited[ni][nj] = 0
solve(0, 0)
print(ans)