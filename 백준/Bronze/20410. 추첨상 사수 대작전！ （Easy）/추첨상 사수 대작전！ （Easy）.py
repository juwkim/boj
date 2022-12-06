m, Seed, X1, X2 = map(float, input().split())

if Seed != X1:
    f = 0
    while True:
        a, q = divmod(X1 - X2 + m * f, Seed - X1)
        if q == 0:
            break
        f += 1
    
    c = X1 - (a * Seed) % m
    print(int(a % m), int(c % m))
else:
    print(1, 0)