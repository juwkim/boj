ans = []
for _ in range(int(input())):
    cur, l = 0, 0
    for c in input():
        if c.isdigit():
            cur = cur * 10 + int(c)
            l += 1
        else:
            if cur or l:
                ans.append(cur)
            cur = 0
            l = 0
    if cur or l:
        ans.append(cur)
print(*sorted(ans))