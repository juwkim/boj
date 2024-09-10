ans = 0
n, k, t0, *l = map(int, open(0).read().split())
for d in l:
    t0 += d + abs(t0 - k) * ((t0 < k) - (t0 > k))
    ans += abs(t0 - k)
print(ans)