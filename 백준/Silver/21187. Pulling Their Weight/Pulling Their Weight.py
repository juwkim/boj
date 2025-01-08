from collections import Counter

n, *w = map(int, open(0))
cnt = Counter(w)
m = sum(k * v for k, v in cnt.items())
a, b, t = 0, cnt[1], 1
while a + b != m:
    t += 1
    a, b = b, b + t * cnt[t]
print(t)