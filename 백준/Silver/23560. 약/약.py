a, b = 2, 1
for _ in range(int(input()) - 1):
    a, b = 2 * a + 2 * b, a + b
print(a)