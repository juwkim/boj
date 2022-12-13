g = lambda: [*map(int, input().split())]

n, r, s = g()
for _ in range(n):
    Map = [input() for _ in range(r)]
    s = [line.index('#') for line in zip(*Map)]
    print(max(s) - min(s))