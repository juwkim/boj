N, M, a, b = map(int, open(0).read().split())
s, n = "S" * M, "N" * M
for _ in range(a):
    print(s)
print('E' * b + 'W' * (M - b))
for _ in range(N - a - 1):
    print(n)