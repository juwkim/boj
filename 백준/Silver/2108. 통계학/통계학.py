import statistics as s
_, *n = map(int, open(0).read().split())
a = sorted(s.multimode(n))
print(round(s.mean(n)), s.median(n), a[0] if len(a) == 1 else a[1], max(n) - min(n))