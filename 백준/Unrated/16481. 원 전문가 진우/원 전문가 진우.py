g = lambda: [*map(int, input().split())]

r1, r2, r3 = g()
r = r1 * r2 * r3 / (r1 * r2 + r2 * r3 + r3 * r1)
print(r)