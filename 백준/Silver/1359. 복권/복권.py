from math import comb
N, M, K = map(int, input().split())
ans = sum(comb(M, i) * comb(N - M, M - i) for i in range(K, M+1)) / comb(N, M)
print(ans)