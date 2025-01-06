pos = lambda x, y: (8 - int(y), ord(x) - ord('a'))

b = [[*input()] for _ in range(8)]
for _ in range(int(input())):
    x1, y1, x2, y2 = input()
    (i1, j1), (i2, j2) = pos(x1, y1), pos(x2, y2)
    print(b[i1][j1], end='')
    b[i2][j2] = b[i1][j1]