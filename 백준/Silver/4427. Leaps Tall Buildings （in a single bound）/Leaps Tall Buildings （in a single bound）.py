import math

while True:
    try:
        n = int(input())
    except:
        break
    hs, ds = [], []
    for _ in range(n):
        h, d = input().split()
        hs.append(int(h))
        ds.append(float(d))
    xs = [0]
    for d in ds:
        xs.append(xs[-1] + d)
    D = xs[-1]
    f = lambda x: x - x * x / D
    theta = math.atan(max(hs[i] / min(f(xs[i]), f(xs[i+1])) for i in range(1, n - 1)))
    angle = math.degrees(theta)
    v = math.sqrt(9.8 * D / math.sin(2 * theta))
    print(angle, v)