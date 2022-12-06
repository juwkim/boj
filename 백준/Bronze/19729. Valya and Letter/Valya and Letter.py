def g(a, b):
    s = 0
    while a > b:
        b *= 2
        s += 1
    return s

n, m, h, w = map(int, input().split())
print(min(g(n, h) + g(m, w), g(n, w) + g(m, h)))