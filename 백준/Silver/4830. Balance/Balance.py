import sys
input = sys.stdin.readline
f = lambda: [*map(float, input().split())]

_, terms, rebalance = map(int, input().split())
fixed_fee, percentage_fee, pricipal = f(), f(), f()
s = sum(pricipal)
ratio = [p / s for p in pricipal]
for i in range(terms):
    if i and i % rebalance == 0:
        s = sum(pricipal)
        pricipal = [r * s for r in ratio]
    for j, a in enumerate(f()):
        pricipal[j] = max(0, pricipal[j] * (1 + a - percentage_fee[j]) - fixed_fee[j])
print(*map(lambda s: "%.2f" % s, pricipal))