input()
ans, cur, prev, now = 0, 0, 0, 'a'
for c in input():
    if c == now:
        cur += 1
    else:
        ans = max(ans, min(prev, cur))
        prev = cur
        cur = 1
        now = c
ans = max(ans, min(prev, cur))
print(ans * 2)