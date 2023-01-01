def g(): return [*map(int, input().split())]

n, m = g()
t = sorted(g())

idx = 0
for l in sorted(g()):
    if idx == n:
        break
    idx += t[idx] <= l
print(idx)