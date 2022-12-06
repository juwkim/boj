N, M = map(int, input().split())
A = {i: i for i in range(1, N+1)}
for _ in range(M):
    x, y = map(int, input().split())
    A[x], A[y] = A[y], A[x]
print(*A.values())