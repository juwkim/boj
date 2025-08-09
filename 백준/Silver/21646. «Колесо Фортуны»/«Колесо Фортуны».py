n, *vals, a, b, k = map(int, open(0).read().split())
ans, L = 0, (a - 1) // k
for t in range(L, min(L + n, (b - 1) // k + 1)):
    i = t % n
    ans = max(ans, vals[i], vals[-i])
print(ans)