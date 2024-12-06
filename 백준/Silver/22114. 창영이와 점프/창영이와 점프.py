N, K, *L = map(int, open(0).read().split())
ans, prv, cur = 2, 0, 1
for num in L:
    if num <= K:
        cur += 1
    else:
        ans = max(ans, prv + cur)
        prv, cur = cur, 1
ans = max(ans, prv + cur)
print(ans)