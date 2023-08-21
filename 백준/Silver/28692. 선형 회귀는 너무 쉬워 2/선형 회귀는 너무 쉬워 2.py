l_x, l_y = [], []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    l_x.append(x)
    l_y.append(y)
Sx, Sy = sum(l_x), sum(l_y)
Sxx = sum(x * x for x in l_x)
Sxy = sum(x * y for x, y in zip(l_x, l_y))

if Sx * Sx == n * Sxx:
    print("EZPZ")
else:
    a2 = (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
    b2 = (Sy - a2 * Sx) / n
    print(a2, b2)