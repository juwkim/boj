g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    input()
    *l, D = g()
    A, B, C = sorted(l)
    if C - B >= D:
        print(A * B * (C - D))
    elif C + B - 2 * A >= D:
        D -= C - B
        r, q = divmod(D, 2)
        B -= r
        print(A * B * (B - q))
    else:
        D -= C + B - 2 * A
        r, q = divmod(D, 3)
        A -= r
        if q == 2:
            print(A * (A - 1) * (A - 1))
        elif q == 1:
            print(A * A * (A - 1))
        else:
            print(A ** 3)