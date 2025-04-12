N, M, X, *a = map(int, open(0).read().split())
cnt, idx = [0] * M, 0
while N and idx < M - 1:
    while idx < M - 1:
        p = min(N, (X - a[-1] * N) // (a[idx] - a[-1]))
        if p:
            break
        idx += 1
    N -= p
    X -= a[idx] * p
    cnt[idx] += p
cnt[-1] = N
print(*cnt)