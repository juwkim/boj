n, k = map(int, input().split())
d, s = map(int, input().split())
t = (n * d - k * s) / (n - k)
print(t if 0 <= t <= 100 else 'impossible')