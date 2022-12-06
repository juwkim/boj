g = lambda: [*map(int, input().split())]

p1, p2, p3 = sorted(g())
c1, c2, c3 = g()

c2, c3 = sorted([c2, c3])
save1 = (p1 + p2 + p3) * c1 / 100
save2 = (p2 * c2 + p3 * c3) / 100
if save1 > save2:
    print('one', '%.2f' % save1)
else:
    print('two', '%.2f' % save2)