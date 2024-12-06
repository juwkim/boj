N, K, A1, A2, B1, B2 = map(int, open(0).read().split())
log, check = [], set()
cur = [*range(1, N + 1)]
while len(log) <= K:
    p = tuple(cur)
    if p in check:
        break
    log.append(p)
    check.add(p)
    cur[A1-1:A2] = cur[A1-1:A2][::-1]
    cur[B1-1:B2] = cur[B1-1:B2][::-1]
i = log.index(p)
ans = log[(K - i) % (len(log) - i) + i]
print(*ans, sep='\n')