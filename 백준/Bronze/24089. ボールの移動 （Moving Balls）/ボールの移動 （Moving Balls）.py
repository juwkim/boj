N, M = map(int, input().split())
d = {i:i for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    d[a] = b
print(*d.values())