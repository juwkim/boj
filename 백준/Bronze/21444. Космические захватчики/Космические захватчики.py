g = lambda: [*map(int, input().split())]

n, p = g()
print(sum(g()) + n - 1 + min(p - 1, n - p))