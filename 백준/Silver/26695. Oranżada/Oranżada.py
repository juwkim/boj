n, k, *a = map(int, open(0).read().split())
ans, st, front = 0, 0, set()
for n in a:
    if n in front: st += 1
    else:
        front.add(n)
        ans += st
        if len(front) == k: break
print((-1, ans)[len(front) == k])