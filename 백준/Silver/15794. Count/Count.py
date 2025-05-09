from collections import Counter

n = int(input())
cnt = Counter(map(int, input().split()))
v = int(input())

ans, min_diff = 1, 1e9
i, j = 0, len(cnt) - 1
a = sorted(cnt)
while i <= j:
    if i == j and cnt[a[i]] < 2:
        break
    total = a[i] + a[j]
    diff = abs(total - v) 
    if diff < min_diff:
        if i == j:
            ans = cnt[a[i]] * (cnt[a[i]] - 1) >> 1
        else:
            ans = cnt[a[i]] * cnt[a[j]]
        min_diff = diff
    elif diff == min_diff:
        if i == j:
            ans += cnt[a[i]] * (cnt[a[i]] - 1) >> 1
        else:
            ans += cnt[a[i]] * cnt[a[j]]
    if total < v:
        i += 1
    else:
        j -= 1
print(ans)