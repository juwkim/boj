g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    h, m, s = g()
    
    A = (h * 3600 + m * 60 + s) / 120
    B = (m * 60 + s) / 10
    C = s * 6
    
    x = max(A - B, B - A)
    y = max(C - B, B - C)
    z = max(C - A, A - C)
    
    x = min(x, 360 - x)
    y = min(y, 360 - y)
    z = min(z, 360 - z)
    print(min(x, y, z))