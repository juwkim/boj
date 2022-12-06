g = lambda: [*map(int, input().split())]

X, Y = g()
print('impossible' if Y&1 else 'possible')