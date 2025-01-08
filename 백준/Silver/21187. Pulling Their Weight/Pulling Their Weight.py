from collections import Counter

m, *a = map(int, open(0).read().split())
cnt, s = Counter(a), sum(a)
cur = 0
for k, v in sorted(cnt.items()):
    if 2 * (cur + v // 2 * k) == s - k * (v & 1):
        print(k)
        break
    if 2 * (cur + v * k) == s:
        print(k + 1)
        break
    cur += v * k