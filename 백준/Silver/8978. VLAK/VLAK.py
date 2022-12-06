g = lambda: [*map(int, input().split())]

N, K = g()
cnt = [[0, [0 for _ in range(26)]] for _ in range(N)]
check = set(range(N))
for _ in range(int(input())):
    s = ord(input()[0]) - 97
    MIN = min(cnt[i][1][s] for i in check)
    idxs = [i for i in range(N) if cnt[i][1][s] == MIN]
    if len(idxs) == 1:
        cnt[idxs[0]][0] += 1
        if cnt[idxs[0]][0] == K:
            check.remove(idxs[0])
        cnt[idxs[0]][1][s] += 1
    else:
        MIN = min(cnt[idx][0] for idx in idxs)
        idxs = [idx for idx in idxs if cnt[idx][0] == MIN]
        cnt[idxs[0]][0] += 1
        if cnt[idxs[0]][0] == K:
            check.remove(idxs[0])
        cnt[idxs[0]][1][s] += 1
for i in range(N):
    print(cnt[i][0], end=' ')