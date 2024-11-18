def num():
    a, b, c, d, e, f = map(int, input().split())
    return 13 * a + 7 * b + 5 * c + 3 * (d + e) + 2 * f

if num() > num() + 1:
    print("cocjr0208")
else:
    print("ekwoo")