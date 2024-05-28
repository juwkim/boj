g = lambda: map(int, input().split())
N, P, Q = g()
f = 1
l = []
for a, b in zip(g(), g()):
    if a == b: l.append(0)
    elif (P - Q) * (a - b) >= 0:
        f = 0
        break
    else:
        q, r = divmod(abs(a - b), abs(Q - P))
        if r or q > 10000:
            f = 0
            break
        l.append(q)
print(("NO", "YES")[f])
if f: print(*l)