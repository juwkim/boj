m, Seed, X1, X2 = map(float, input().split())

if Seed != X1:
    f, g = 0, 0
    while True:
        a = (X1 - X2 + m * f) / (Seed - X1)
        if a == int(a):
            break
        f += 1
        
    while True:
        c = (Seed * (X2 + m * g) - X1 * (X1 + m * (f + g))) / (Seed - X1)
        if c == int(c):
            break
        g += 1
    print(int(a%m), int(c%m))
else:
    print(1, 0)