n, l, w, x, y, a = map(int, input().split())
if n > ((w - a) // y) * (l // x):
    print(-1)
else:
    col = l // x
    row = (n + col - 1) // col
    alley = (w - row * y) // a
    print(min(n, min(row, 2 * alley) * col))