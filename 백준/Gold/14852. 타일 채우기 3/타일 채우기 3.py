a, b, c = 2, 7, 22
for _ in range(int(input()) - 1):
    a, b, c = b, c, (3 * c + b - a) % 1000000007
print(a)