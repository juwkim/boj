N, M = map(int, input().split())
for i in range(N):
    print(*range(1+M*i, 1+M*i+M))