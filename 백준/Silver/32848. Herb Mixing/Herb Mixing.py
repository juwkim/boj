green, red = map(int, input().split())
if red >= green:
    print(green * 10)
else:
    q, r = divmod(green - red, 3)
    print(red * 10 + q * 10 + (0, 1, 3)[r])