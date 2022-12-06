g = lambda: [*map(int, input().split())]

while n:= int(input()):
    x1, y1, z1, r = zip(*[g() for _ in range(n)])
    x2 = [i + j for i, j in zip(x1, r)]
    y2 = [i + j for i, j in zip(y1, r)]
    z2 = [i + j for i, j in zip(z1, r)]
    ans = max(0, min(x2) - max(x1)) * max(0, min(y2) - max(y1)) * max(0, min(z2) - max(z1))
    print(ans)