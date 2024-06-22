*l, p = map(int, input().split())
n, m = sorted(l)
print(("NO", "YES")[p % 2 == 0 and 0 < 2 * (n + m) - p // 2 < m])