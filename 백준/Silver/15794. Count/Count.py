from collections import Counter

n = int(input())
cnt = Counter(map(int, input().split()))
v = int(input())
ans, min_diff = 1, 1e9
i, j = 0, len(cnt) - 1
a = sorted(cnt)
while i < j:
    total = a[i] + a[j]
    diff = abs(total - v) 
    if diff < min_diff:
        ans, min_diff = cnt[a[i]] * cnt[a[j]], diff
    elif diff == min_diff:
        ans += cnt[a[i]] * cnt[a[j]]
    if total < v:
        i += 1
    else:
        j -= 1
if cnt[a[i]] > 1:
    diff = abs(a[i] * 2 - v)
    if diff < min_diff:
        ans = cnt[a[i]] * (cnt[a[i]] - 1) >> 1
    elif diff == min_diff:
        ans += cnt[a[i]] * (cnt[a[i]] - 1) >> 1
print(ans)