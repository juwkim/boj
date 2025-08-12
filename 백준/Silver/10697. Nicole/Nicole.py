import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, int(input()) + 1):
    N, M = g()
    weights = g()
    edges = [bytearray(N + 1) for _ in range(N + 1)]
    for i in range(M):
        F, T = g()
        edges[F][T] = 1
        edges[T][F] = 1
    ans = -1
    visited = bytearray(N + 1)
    def solve(i, total, visited_cnt):
        global ans
        if i == N + 1:
            if visited_cnt >= 2:
                ans = max(ans, total)
            return
        solve(i + 1, total, visited_cnt)
        if all(not visited[j] or not edges[i][j] for j in range(1, i)):
            visited[i] = 1
            solve(i + 1, total + weights[i - 1], visited_cnt + 1)
            visited[i] = 0
    solve(1, 0, 0)
    print(f"Case {tc}: {ans}")