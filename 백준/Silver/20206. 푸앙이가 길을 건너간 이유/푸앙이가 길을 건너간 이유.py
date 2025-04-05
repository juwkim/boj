A, B, C, X1, X2, Y1, Y2 = map(int, open(0).read().split())
l = lambda x, y: A * x + B * y + C
s = l(X1, Y1), l(X1, Y2), l(X2, Y1), l(X2, Y2)
print(("Poor", "Lucky")[all(i >= 0 for i in s) or all(i <= 0 for i in s)])