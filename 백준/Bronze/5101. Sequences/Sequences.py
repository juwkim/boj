while True:
    a, d, k = map(int, input().split())
    if (a, d, k) == (0, 0, 0):
        break
    t = (k-a)/d + 1
    print(int(t) if t == int(t) and t > 0 else 'X')