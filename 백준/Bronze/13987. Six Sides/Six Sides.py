from itertools import product
g = lambda: [*map(int, input().split())]
game = [*map(lambda x: (x[0] > x[1]) - (x[0] < x[1]), product(g(), g()))]
a, b = game.count(1), game.count(-1)
print(f'{a/(a+b):#.5f}')