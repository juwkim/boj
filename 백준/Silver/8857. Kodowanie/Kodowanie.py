for _ in range(int(input())):
    a, b = 0, 1
    for _ in range(int(input()) - 1):
        a, b = a + b, a
    print(a + b)