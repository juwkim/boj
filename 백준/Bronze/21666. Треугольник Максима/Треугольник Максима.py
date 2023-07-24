l, h = 30, 4000
n = int(input())
prev = float(input())
for _ in range(n - 1):
    cur, what = input().split()
    cur = float(cur)
    if cur == prev:
        continue
    if what == 'closer':
        if cur < prev:
            h = min(h, (cur + prev) / 2)
        else:
            l = max(l, (cur + prev) / 2)
    else:
        if cur < prev:
            l = max(l, (cur + prev) / 2)
        else:
            h = min(h, (cur + prev) / 2)
    prev = cur
print(min(l, 4000), max(30, h))