import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M, K = g()
A = [g() for _ in range(N)]
ans = -40000
l = []
def solve(o, c = 0):
    if o == N * M:
        return
    i, j = divmod(o, M)
    if (i - 1, j) not in l and (i, j - 1) not in l:
        if len(l) == K - 1:
            global ans
            ans = max(ans, c + A[i][j])
        else:
            l.append((i, j))
            solve(o + 1, c + A[i][j])
            l.pop()
    solve(o + 1, c)
solve(0)
print(ans)