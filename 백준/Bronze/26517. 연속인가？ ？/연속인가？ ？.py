g = lambda: [*map(int, input().split())]

k = int(input())
a, b, c, d = g()
if (a - c) * k + b - d == 0:
    print('Yes', a * k + b)
else:
    print('No')