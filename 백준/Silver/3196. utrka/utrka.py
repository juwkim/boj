K, N, M = map(int, input().split())
pos = [[-1, -1] for _ in range(N)]
for i in range(M):
    X, Y = map(lambda x: int(x) - 1, input().split())
    if (Y - pos[X][0]) % K == 1:
        pos[X][0] += 1
        pos[X][1] = i
ans = sorted(range(1, N + 1), key=lambda i: (-pos[i-1][0], pos[i-1][1]))
print(*ans)