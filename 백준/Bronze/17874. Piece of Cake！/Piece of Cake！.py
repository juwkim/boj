n, h, v = map(int, input().split())
print(4 * max(h, n - h) * max(v, n - v))