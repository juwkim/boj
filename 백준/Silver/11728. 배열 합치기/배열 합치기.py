input()
g = lambda: [*map(int, input().split())]
print(*sorted(g() + g()))