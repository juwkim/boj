N, K, S, *P = map(int, open(0).read().split())

def check(limit):
    acc, cnt = 0, 1
    for x in P:
        if (acc + x + S - 1) // S <= limit:
            acc += x
        else:
            cnt += 1
            acc = x
            if cnt > K:
                return False
    return True

lo = (max(P) + S - 1) // S - 1
hi = (sum(P) + S - 1) // S
while hi > lo + 1:
    mid = lo + hi >> 1
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)