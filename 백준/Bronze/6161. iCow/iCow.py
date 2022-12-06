N, T = map(int, input().split())
R = [int(input()) for _ in range(N)]
for _ in range(T):
    t = R.index(s:=max(R))
    r, q = divmod(s, N-1)
    for i in range(q + (t < q)):
        R[i] += r + 1
    for i in range(q + (t < q), N):
        R[i] += r
    R[t] = 0
    print(t+1)