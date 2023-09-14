a, b, c, d = map(int, input().split())
if a != d and b != c:
    print("EI")
else:
    print("JAH")
    if a != d:
        d = a
    elif b != c:
        b = c
    print(a, b, c, d)