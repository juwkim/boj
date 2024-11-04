_, *a = map(int, open(0).read().split())
cnt = [0] * (m := max(a) + 1)
for n in a: cnt[n] += 1
ans = 0
for i in range(1, m):
    t = -1
    for j in range(i, m, i): t += cnt[j]
    ans += t * cnt[i]
print(ans)