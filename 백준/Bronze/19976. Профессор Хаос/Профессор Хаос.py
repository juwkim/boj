cur, b, c, d, k = map(int, input().split())
for _ in range(k):
    nxt = min(max(0, cur * b - c), d)
    if nxt == cur:
        break
    cur = nxt
print(cur)