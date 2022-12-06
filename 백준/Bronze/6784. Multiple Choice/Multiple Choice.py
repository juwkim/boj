N = int(input())
g = lambda: [input() for _ in range(N)]
print(sum(x == y for x, y in zip(g(), g())))