a, b, c, u0, u1, u2 = map(int, input().split())
l = ((a + b, a + b, 0), (2 * a + c, 2 * a + c, 0), (2 * b + c, 2 * b + c, 0), (a, c, b), (b, c, a), (a + c, c, a), (b + c, c, b))
ans = min(sum(s * t for s, t in zip(p, (1/u0, 1/u1, 1/u2))) for p in l)
print(ans)