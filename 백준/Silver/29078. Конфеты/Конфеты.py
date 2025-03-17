from collections import Counter

n, *p = map(int, open(0).read().split())
ans, cnt = 0, Counter()
l = 0
for i in range(n):
    if p[i] not in cnt:
        while len(cnt) == 2:
            cnt[p[l]] -= 1
            if cnt[p[l]] == 0:
                cnt.pop(p[l])
            l += 1
    cnt[p[i]] += 1
    if len(cnt) == 2:
        ans = max(ans, i - l + 1)
print(ans)