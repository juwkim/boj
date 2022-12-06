I, P = int, print
t = [input().split() for _ in range(I(input()))]
if I(t[0][0]) < I(t[0][1]):
    if I(t[0][0]) < I(t[1][0]):
        for r in t: P(*r)
    else:
        for r in [*zip(*t)]: P(*r[::-1])
else:
    if I(t[0][0]) > I(t[1][0]):
        for r in t[::-1]: P(*r[::-1])
    else:
        for r in [*zip(*t)][::-1]: P(*r)