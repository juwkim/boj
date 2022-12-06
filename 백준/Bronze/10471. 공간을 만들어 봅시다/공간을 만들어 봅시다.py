from itertools import combinations
g = lambda: map(int, input().split())
W, _ = g()
print(*sorted(set(map(lambda x: abs(x[0]-x[1]), combinations([0, *g(), W], 2)))))