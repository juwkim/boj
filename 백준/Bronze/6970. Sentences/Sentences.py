from itertools import product
for _ in range(int(input())):
    a, b, c = [int(input()) for _ in range(3)]
    x = [input() for _ in range(a)]
    y = [input() for _ in range(b)]
    z = [input() for _ in range(c)]
    for l in product(x, y, z):
        print(*l, end='.\n')
    print()