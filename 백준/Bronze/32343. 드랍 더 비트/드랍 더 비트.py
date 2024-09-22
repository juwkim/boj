N, x, y = map(int, open(0).read().split())
print((1 << N) - (1 << abs(x + y - N)))