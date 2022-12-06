g = lambda: [*map(int, input().split())]
n, k, m = g()
for _ in range(m):
    print()
    print(*range(1, k+1))