a, b = 2, 1
for _ in range(int(input()) - 1):
    a, b = 2 * (a + b) % 1000000007, a
print((a + b) % 1000000007)