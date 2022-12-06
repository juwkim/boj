g = lambda: [*map(int, input().split())]
Mw, Mb = g()
Tw, Tb = g()
Pw, Pb = g()

a = min(Mw, Tb, Pw)
b = min(Mb, Tw, Pb)

if a == b:
    ans = a + b
else:
    ans = 2 * min(a, b) + 1

print(ans)