def solve():
    for j in range(M):
        for i in range(N):
            res[i] += buf[i][j]
            if res[i] >= K:
                return i + 1, j + 1

N, M, K = map(int, input().split())
res = [0] * N
buf = [[*map(int, input().split())] for _ in range(N)]
print(*solve())