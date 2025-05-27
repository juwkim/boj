N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for mask in range(1, (1 << N) - 1):
    A, B = [], []
    for i in range(N):
        if (mask >> i) & 1:
            A.append(i)
        else:
            B.append(i)
    ans = max(ans, sum(C[i][j] for i in A for j in B))
print(ans)