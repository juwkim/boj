d1, d2, x = map(int, input().split())
d1, d2 = sorted([d1, d2])

ans = 100 * d1 * d2 / (x * d1 + (100 - x) * d2)
print(ans)