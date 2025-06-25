def solve():
    N, M, K, *d = map(int, open(0).read().split())
    ans = [0] * K
    cur = -1
    for i in sorted(range(N), key=lambda i: d[i]):
        if M > K - cur - 2:
            break
        if M < d[i] - 1:
            print(-1)
            return
        M -= d[i] - 1
        cur += d[i]
        ans[cur] = i + 1
    print(*ans)
solve()