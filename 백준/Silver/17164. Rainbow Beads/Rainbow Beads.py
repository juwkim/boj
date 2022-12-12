input()
ans, cnt, prev = 0, 0, ''
for c in input():
    if c == 'V':
        ans = max(ans, cnt)
        cnt = 0
    elif c == prev:
        ans = max(ans, cnt)
        cnt = 1
    else:
        cnt += 1
    prev = c
ans = max(ans, cnt)
print(ans)