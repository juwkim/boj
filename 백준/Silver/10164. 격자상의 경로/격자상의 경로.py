from math import comb

N, M, K = map(int, input().split())
if K:
    r, c = divmod(K - 1, M)
    ans = comb(r + c, r) * comb(N + M - 2 - r - c, N - 1 - r)
else:
    ans = comb(N + M - 2, N - 1)
print(ans)