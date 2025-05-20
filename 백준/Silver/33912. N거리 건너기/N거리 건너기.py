N, M, *A = map(int, open(0).read().split())
dic = {a: i for i, a in enumerate(A)}
CW, CCW = 0, 0
for i in range(1, M):
    r = CW % N
    CW += dic[i] + 1 - r + N * (r > dic[i])
for i in range(N, M - 1, -1):
    r = dic[i]
    if CCW % N > r:
        CCW += r + 1 - CCW % N + N
    else:
        CCW += r + 1 - CCW % N
print(("EQ", "CW", "CCW")[(CW < CCW) - (CW > CCW)])