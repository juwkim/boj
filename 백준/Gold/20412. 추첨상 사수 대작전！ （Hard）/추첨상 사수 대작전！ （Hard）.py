m, Seed, X1, X2 = map(int, input().split())

a = (X1 - X2) * pow(Seed - X1, m - 2, m) % m
c = (X1 - (a * Seed) % m) % m
print(a, c)