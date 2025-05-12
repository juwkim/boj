N, *a = map(int, open(0).read().split())
a.sort()
check, cnt = bytearray(N + 1), 0
cur, idx = 0, 0
for i in range(N + 1):
    while idx < N and a[idx] < i:
        if check[a[idx]] == 0:
            cnt += 1
            check[a[idx]] = 1
        idx += 1
    while idx < N and a[idx] == i:
        cur += 1
        idx += 1
    print(max(cur, i - cnt))
    if cur:
        check[i] = 1
        cur = 0
        cnt += 1