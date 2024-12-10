x, b = map(int, input().split())
s = input()
r = x // (3 * b)
if r * 3 * b == x:
    print(2 * r)
elif r * 3 * b + b * (1, 2)[s == 'T'] >= x:
    print(2 * r + 1)
else:
    print(2 * r + 2)