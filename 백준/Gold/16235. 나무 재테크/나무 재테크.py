import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, K = g()
A = [g() for _ in range(N)]
ground = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = g()
    tree[x - 1][y - 1].append(z)

for _ in range(K):
    dead = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                k = 0
                while k < len(tree[i][j]) and ground[i][j] >= tree[i][j][k]:
                    ground[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                    k += 1
                while k < len(tree[i][j]):
                    ground[i][j] += tree[i][j].pop() // 2
            ground[i][j] += A[i][j]
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].append(1)
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)