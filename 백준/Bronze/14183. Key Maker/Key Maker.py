g = lambda: [*map(int, input().split())]
while True:
    m, n = g()
    if (m, n) == (0, 0):
        break
    customer, keys = g(), [g() for _ in range(n)]
    print(sum(all(x >= y for x, y in zip(customer, key)) for key in keys))