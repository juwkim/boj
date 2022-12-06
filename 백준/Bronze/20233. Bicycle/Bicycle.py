a, x, b, y, T = [int(input()) for _ in [0] * 5]
print(a + 21 * x * max(T - 30, 0), b + 21 * y * max(T - 45, 0))