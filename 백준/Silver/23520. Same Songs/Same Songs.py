n, *playlist = map(int, open(0).read().split())
l = []
check = set()
cnt = 0
for p in playlist:
    if l and l[-1] == p:
        l.append(p)
        check = set()
        cnt += 1
    elif p in check:
        l.extend((p, p))
        check = set()
        cnt += 1
    else:
        check.add(p)
print(len(l), cnt)
print(*l)