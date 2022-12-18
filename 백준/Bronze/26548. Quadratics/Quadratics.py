g = lambda: [*map(float, input().split())]

for _ in range(int(input())):
    a, b, c = g()
    x1 = (-b + (b * b - 4 * a * c) ** .5) / (2 * a)
    x2 = (-b - (b * b - 4 * a * c) ** .5) / (2 * a)
    print("%.3f, %.3f" % (x1, x2))