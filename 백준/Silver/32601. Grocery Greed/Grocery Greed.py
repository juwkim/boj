input()
ans, cnt = 0, [0, 0, 0, 0, 0]
for p in input().split():
    a, b = map(int, p.split('.'))
    ans += 100 * a + b
    cnt[b % 5] += 1
ans -= cnt[1] + 2 * cnt[2] + 2 * (l := min(cnt[3], cnt[4]))
ans -= (cnt[3] - l) // 2 + (cnt[4] - l) // 3 * 2
q, r = divmod(ans, 100)
print(f"{q}.{r:02d}")