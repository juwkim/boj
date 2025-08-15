g = lambda: [*map(int, input().split())]
from collections import Counter

n = int(input())
cnt = Counter(g())
m = int(input())
a = g()
for i in range(n):
    cnt[a[i]] -= 1
diff = sum(v != 0 for v in cnt.values())
ans = "NO"
if diff == 0:
    ans = "YES\n1"
else:
    for s in range(n, m):
        p, q = cnt[a[s]], cnt[a[s - n]]
        cnt[a[s]] -= 1
        cnt[a[s - n]] += 1
        if p == 0 and cnt[a[s]]:
            diff += 1
        elif p and cnt[a[s]] == 0:
            diff -= 1
        if a[s] != a[s - n]:
            if q == 0 and cnt[a[s - n]]:
                diff += 1
            elif q and cnt[a[s - n]] == 0:
                diff -= 1
        if diff == 0:
            ans = f"YES\n{s - n + 2}"
            break
print(ans)