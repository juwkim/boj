g = lambda: [*map(int, input().split())]

a, b, c, d = sorted(g() for _ in range(4))
if a == b or b == c or c == d:
    print('NIE')
elif a[0] == b[0] and a[1] == c[1] and b[1] == d[1] and c[0] == d[0] and c[0] - a[0] == b[1] - a[1]:
    print('TAK')
else:
    print('NIE')