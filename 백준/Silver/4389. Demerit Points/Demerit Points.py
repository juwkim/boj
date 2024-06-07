def pr(t, p):
    y, m, d = t // 10000, t // 100 % 100, t % 100
    if p == 0:
        print(f"{y}-{m:02d}-{d:02d} No merit or demerit points.")
    elif p < 0:
        print(f"{y}-{m:02d}-{d:02d} {-p} demerit point(s).")
    else:
        print(f"{y}-{m:02d}-{d:02d} {p} merit point(s).")

t, *l = open(0).readlines()
p, t = 0, int(t)
pr(t, p)
for s in l:
    cur, pp = map(int, s.split())
    while True:
        if 0 <= p < 5 and t + 20000 <= cur:
            t += 20000
            p += 1
        elif p < 0 and t + 10000 <= cur:
            t += 10000
            p = max((p + 1) // 2, min(0, p + 2))
        else:
            break
        pr(t, p)
    t = cur
    if p <= 0: p -= pp
    elif pp >= 2 * p: p = 2 * p - pp
    else: p -= (pp + 1) // 2
    pr(t, p)
while p != 5:
    if 0 <= p < 5:
        t += 20000
        p += 1
    else:
        t += 10000
        p = max((p + 1) // 2, min(0, p + 2))
    pr(t, p)