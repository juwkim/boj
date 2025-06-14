import sys
input = sys.stdin.readline

N, M = map(int, input().split())
colors = [[*map(float, input().split())] for _ in range(N)]
dist = [[0] * N for _ in range(N)]
for i in range(N - 1):
    Li, ai, bi = colors[i]
    for j in range(i + 1, N):
        Lj, aj, bj = colors[j]
        d = (Li - Lj)**2 + (ai - aj)**2 + (bi - bj)**2
        dist[i][j] = d
        dist[j][i] = d

selected = []
def solve(start, cnt, acc_sum):
    global ans
    if cnt == M:
        ans = max(ans, acc_sum)
        return
    if N - start < M - cnt:
        return
    for i in range(start, N):
        add = sum(dist[i][j] for j in selected)
        selected.append(i)
        solve(i + 1, cnt + 1, acc_sum + add)
        selected.pop()
ans = 0
solve(0, 0, 0)
print(ans)