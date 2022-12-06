while True:
    a, b, c = sorted(map(int, input().split()))
    if (a, b, c) == (0, 0, 0):
        break
    if a + b <= c:
        print('Invalid')
    elif a == c:
        print('Equilateral')
    elif a == b or b == c:
        print('Isosceles')
    else:
        print('Scalene')