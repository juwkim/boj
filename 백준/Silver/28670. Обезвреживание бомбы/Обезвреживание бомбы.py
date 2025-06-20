from collections import Counter

n, k, *a = map(int, open(0).read().split())
cnt = Counter(a)
ans = 0
for x in cnt:
    y = k - x
    if y not in cnt:
        continue
    if x == y:
        ans += cnt[x] - 1
    elif x < y:
        ans += min(cnt[x], cnt[y])
print(ans)