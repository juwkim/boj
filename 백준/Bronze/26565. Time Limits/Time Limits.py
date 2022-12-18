g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    n, s = g()
    print((max(g()) * s + 999) // 1000)