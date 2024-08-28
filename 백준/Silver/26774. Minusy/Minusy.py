ans = 0
cur, *l = map(len, input().split('+'))
cur //= 2
for s in l:
    if s & 1:
        ans = max(ans, cur + s // 2 + 1)
        cur = s // 2
    else:
        cur += s // 2 + 1
ans = max(ans, cur)
print(ans)