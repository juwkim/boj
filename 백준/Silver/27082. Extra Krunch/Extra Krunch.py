ans, check = [], set("AEIOU")
for word in input().split():
    l = []
    for c in word:
        if c in ".,?":
            l.append(c)
        elif c not in check:
            l.append(c)
            check.add(c)
    if l:
        p = "".join(l)
        if ans and p[0] in ".,?":
            ans[-1] += p
        else:
            ans.append(p)
print(*ans)