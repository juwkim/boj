from math import comb
N, K, M = map(int, input().split())
ans = 1
while N:
    r1, q1 = divmod(N, M)
    r2, q2 = divmod(K, M)
    ans = ans * comb(q1, q2) % M
    N, K = r1, r2
print(ans)