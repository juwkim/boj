def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


g = lambda: [*map(int, input().split())]
min_y = 100000
for _ in range(int(input())):
    y, c1, c2 = g()
    next_y = y + c1 * c2 // gcd(c1, c2)
    min_y = min(min_y, next_y)
print(min_y)