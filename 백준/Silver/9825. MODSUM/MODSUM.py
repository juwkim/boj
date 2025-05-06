n, *rest = map(int, input().split())
ranges = [(rest[i], rest[i+1]) for i in range(0, len(rest), 2)]
l = n * 100
dp = [0] * (l + 1)
dp[0] = 1
for v, w in ranges:
    ndp = [0] * (l + 1)
    for s in range(l - v, -1, -1):
        if dp[s]:
            for x in range(w, v - 1, -1):
                if s + x <= l:
                    ndp[s + x] += dp[s]
    dp = ndp
print(sum(dp[s] * ((s ** 4 + 2 * s ** 2) % 5 + 1) for s in range(l + 1)))