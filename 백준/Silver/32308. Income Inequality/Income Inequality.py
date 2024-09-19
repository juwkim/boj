n, *m = map(int, open(0).read().split())
total, y = sum(m), 0
ans = 0
for x, num in enumerate(sorted(m, reverse=True), 1):
    y += num
    ans = max(ans, (y / total - x / n) * 100)
print(ans)