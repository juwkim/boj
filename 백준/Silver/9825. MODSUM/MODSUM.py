n, *rest = map(int, input().split())
ranges = [(rest[i], rest[i+1]) for i in range(0, len(rest), 2)]
l = n * 100
dp = [1] + [0] * l
for v, w in ranges:
    for s in range(l - v, -1, -1):
        if dp[s]:
            cnt, dp[s] = dp[s], 0
            for x in range(w, v - 1, -1):
                if s + x <= l:
                    dp[s + x] += cnt
print(sum(dp[s] * ((s ** 4 + 2 * s ** 2) % 5 + 1) for s in range(l + 1)))