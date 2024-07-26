n, *a = map(int, open(0).read().split())
x, y = [0] * n, [0] * n
for j, (i, num) in enumerate(sorted(enumerate(a), key=lambda x: (x[1], x[0])), 1):
    x[i], y[i] = j, num
for xi, yi in zip(x, y):
    print(xi, yi)