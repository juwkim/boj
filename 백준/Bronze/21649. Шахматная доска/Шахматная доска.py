g = lambda: [*map(int, input().split())]

m, n, *l = g()
if m * n % 2 == 0:
    print('equal')
elif sum(l) & 1:
    print('white')
else:
    print('black')