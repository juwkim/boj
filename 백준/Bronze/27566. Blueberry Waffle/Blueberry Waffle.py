r, f = map(int, input().split())

if r / 2 < f % (2 * r) < r + r / 2:
    print('down')
else:
    print('up')