import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M, A, B = g()
T, L, H = g(), {*g()}, {*g()}
ans, good, bad = 0, 0, 0
for t in T:
    if t in L:
        if bad >= 3:
            ans -= bad
        bad = 0
        good += 1
    elif t in H:
        if good >= 3:
            ans += good
        good = 0
        bad += 1
    else:
        if good >= 3:
            ans += good
        if bad >= 3:
            ans -= bad
        good, bad = 0, 0
if good >= 3:
    ans += good
if bad >= 3:
    ans -= bad
print(ans)