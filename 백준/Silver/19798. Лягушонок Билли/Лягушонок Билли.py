from collections import Counter

n, *a = map(int, open(0).read().split())
ans, cnt = 0, Counter(a)
minus = 0
for k, v in sorted(cnt.items(), reverse=True):
    ans += max(0, k - minus) * v
    minus += v
print(ans)