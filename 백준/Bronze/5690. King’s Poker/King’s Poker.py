g = lambda: [*map(int, input().split())]

while sum(s:= g()):
    a, b, c = sorted(s)
    if a == b == c:
        if a == 13:
            print("*")
        else:
            a += 1
            print(a, a, a)
    elif a == b:
        if c == 13:
            print(1, a + 1, b + 1)
        else:
            print(a, b, c + 1)
    elif b == c:
        if a + 1 == b:
            if b == 13:
                print(1, 1, 1)
            else:
                print(b, c, a + 2)
        else:
            print(a + 1, b, c)
    else:
        print(1, 1, 2)