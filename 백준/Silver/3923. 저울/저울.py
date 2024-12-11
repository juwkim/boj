import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    x, y = None, None
    i = (c + a - 1) // a
    while True:
        j, r = divmod(a * i - c, b)
        if r == 0:
            x, y = i, j
            break
        i += 1
    j = (c + b - 1) // b
    while True:
        i, r = divmod(b * j - c, a)
        if r == 0:
            if i + j < x + y or (i + j == x + y and i * a + j * b < x * a + y * b):
                x, y = i, j
            break
        j += 1
    for i in range(c // a + 1):
        j, r = divmod(c - a * i, b)
        if r == 0:
            if i + j < x + y or (i + j == x + y and i * a + j * b < x * a + y * b):
                x, y = i, j
    print(x, y)