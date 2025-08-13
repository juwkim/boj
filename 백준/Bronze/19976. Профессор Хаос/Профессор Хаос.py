cur, b, c, d, k = map(int, input().split())
while k and (nxt:=min(max(0, cur * b - c), d)) != cur:
    cur = nxt
    k -= 1
print(cur)