a, b, c = 0, 0, 1
for _ in range(int(input())):
    a, b, c = a - c, b + c, 2 * a - 2 * b + c
print(a + b + c)