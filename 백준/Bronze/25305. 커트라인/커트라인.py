g = lambda: [*map(int, input().split())]
N, k = g()
print(sorted(g())[-k]) 