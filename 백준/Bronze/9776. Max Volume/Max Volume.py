ans = 0
pi = 3.14159
for _ in range(int(input())):
    t, r, *h = input().split()
    r = float(r)
    if h:
        h = float(h[0])
    if t == 'S':
        V = 4 * pi * r ** 3 / 3
    elif t == 'C':
        V = pi * r * r * h / 3
    else:
        V = pi * r * r * h
    ans = max(ans, V)
print(f"{ans:.3f}")