N, K = map(int, input().split())
for i in range(N):
    buf = []
    for num in map(int, input().split()):
        buf += [num] * K
    for _ in range(K):
        print(*buf)