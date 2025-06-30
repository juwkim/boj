a, b, x = map(int, input().split())
if x <= 1000 * a:
    print(1000)
else:
    t = (x + 1000 * b - 1) // (1000 * (a + b))
    print(min(1000, x / (t * (a + b) - a)))