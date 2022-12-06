g = lambda: [*map(int, input().split())]

while True:
    try:
        n, *l = g()
        l += l[:2]
        print(n, end=' ')
        for i in range(0, 2*n, 2):
            x1, y1, x2, y2 = l[i:i+4]
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            print('%.6f %.6f' % (x, y), end=' ')
    except:
        break