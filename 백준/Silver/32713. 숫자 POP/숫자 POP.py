N, K, *A = map(int, open(0).read().split())
d = {}
for key in {*A}:
    px = [0] * (N + 1)
    for i in range(N):
        px[i + 1] = px[i] + (A[i] == key)
    d[key] = px
ans = 1
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] != A[j]:
            continue
        v = A[i]
        if d[v][j + 1] - d[v][i] > j - i - K:
            ans = max(ans, d[v][j + 1] - d[v][i])
print(ans)