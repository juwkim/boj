import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def check():
    for i in range(N):
        pos = i
        for j in range(H):
            pos += ladder[pos][j]
        if pos != i:
            return False
    return True

N, M, H = g()
ladder = [[0] * H for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    ladder[b][a] = 1
    ladder[b + 1][a] = -1

ans = -1
def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt) if ans != -1 else cnt
        return
    if cnt == 3:
        return
    for i in range(x, N - 1):
        k = y if i == x else 0
        for j in range(k, H):
            if ladder[i][j] or ladder[i + 1][j]:
                continue
            ladder[i][j] = 1
            ladder[i + 1][j] = -1
            dfs(cnt + 1, i, j + 1)
            ladder[i][j] = 0
            ladder[i + 1][j] = 0
dfs(0, 0, 0)
print(ans)