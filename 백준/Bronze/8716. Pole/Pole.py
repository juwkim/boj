g = lambda: map(int, input().split())
def h(a, b, c, d):
    if a*b >= 0:
        return 0
    else:
        return min(abs(a), abs(b), c, d)
X1, Y1, X2, Y2 = g()
X3, Y3, X4, Y4 = g()
print(h(X4-X1, X3-X2, X4 - X3, X2 - X1)*h(Y4-Y1, Y3-Y2, Y3 - Y4, Y1 - Y2))