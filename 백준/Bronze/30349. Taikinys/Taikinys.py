M, N, A, B, X, Y = map(int, open(0).read().split())
ans = 1e9
for i in range(X, X + M + 1):
    for j in range(Y, Y + N + 1):
        if 0 <= i < A and 0 <= j < B:
            ans = min(ans, i + j)
print(ans if ans < 1e9 else "NEPATAIKYS")