a, b, c = map(float, input().split())
if abs(a - c) < 1e-10:
    print("%.4f" % (2 * a * (a + b)))
else:
    print(0)