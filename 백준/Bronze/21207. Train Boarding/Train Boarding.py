N, L, P = map(int,input().split())
res = [0] * (N)
m = 0
for _ in range(P):
    r, q = divmod(int(input()), L)
    if r < N:
        res[r] += 1
        m = max(m, abs(q - L // 2))
    else:
        res[N-1] += 1
        m = max(m, q + L // 2 + (r - N) * L)
print(m, max(res))