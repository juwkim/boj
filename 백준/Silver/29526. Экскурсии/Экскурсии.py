from collections import Counter

n, k, *a = map(int, open(0).read().split())
cnt = Counter(a[:k])
unique = len(cnt)
ans, max_unique = 1, unique
for i in range(1, n - k + 1):
    s, t = a[i - 1], a[i + k - 1]
    cnt[s] -= 1
    if cnt[s] == 0: unique -= 1
    if cnt[t] == 0: unique += 1
    cnt[t] += 1
    if unique > max_unique:
        ans, max_unique = i + 1, unique
print(ans)