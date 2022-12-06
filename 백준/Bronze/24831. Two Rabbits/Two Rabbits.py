for _ in range(int(input())):
    x, y, a, b = map(int, input().split())
    print([-1, (y - x) // (a + b)][(y - x) % (a + b) == 0])