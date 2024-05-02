n, k, *a = map(int, open(0).read().split())
ans, st, fr = 0, 0, set()
for n in a:
    if n in fr: st += 1
    else:
        fr.add(n)
        ans += st
        if len(fr) == k: break
print((-1, ans)[len(fr) == k])