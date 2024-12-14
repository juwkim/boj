g = lambda: map(int, input().split())

N, M = g()
mat = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = g()
    mat[a - 1][b - 1] = 1
    mat[b - 1][a - 1] = 1
ans = 0
def solve(i, pizza):
    global ans
    if i == N:
        ans += 1
        return
    solve(i + 1, pizza)
    if all(not pizza & (1 << j) or mat[i][j] == 0 for j in range(i)):
        solve(i + 1, pizza | (1 << i))
solve(0, 0)
print(ans)