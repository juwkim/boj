a, b, m = 1, 0, 1000000007
for _ in range(int(input())):
    a, b = 2 * (a + b) % m, a
print((a + b) % m)