a, b, h, w = map(int, input().split())
x, y = (h + a - 1) // a, (w + b - 1) // b
print(x * y)