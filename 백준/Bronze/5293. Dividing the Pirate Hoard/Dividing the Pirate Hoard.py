N, M = map(int, input().split())
for _ in range(M):
    q, r = divmod(N, M)
    print(q + r, end=' ')
    N = q * (M - 1)
print(f'\n{N}\n')