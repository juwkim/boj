g = lambda:[*map(int, input().split())]
game = [*zip(g(), g())]
A = sum(x > y for x, y in game)
B = sum(x < y for x, y in game)
print('A' if A > B else 'B' if A < B else 'D')