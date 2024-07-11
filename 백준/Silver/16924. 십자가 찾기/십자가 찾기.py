import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
a = [input() for _ in range(N)]
visited = [bytearray(M) for _ in range(N)]
ans = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if a[i][j] == '.':
            continue
        l = 1
        while l <= min(i, j, N - 1 - i, M - 1 - j) and a[i][j - l] == a[i][j + l] == a[i - l][j] == a[i + l][j] == '*':
            l += 1
        l -= 1
        if l:
            ans.append((i + 1, j + 1, l))
            for x in range(i - l, i + l + 1):
                visited[x][j] = 1
            for y in range(j - l, j + l + 1):
                visited[i][y] = 1
for i in range(N):
    for j in range(M):
        if a[i][j] == '*' and not visited[i][j]:
            print(-1)
            exit()
print(len(ans))
for x, y, l in ans:
    print(x, y, l)