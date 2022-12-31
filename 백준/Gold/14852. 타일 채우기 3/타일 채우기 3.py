a, b, c = 1, 2, 7
for _ in range(int(input())):
    a, b, c = b, c, (3 * c + b - a) % 1000000007
print(a)