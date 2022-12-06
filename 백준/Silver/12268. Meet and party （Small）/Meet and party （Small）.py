g = lambda: [*map(int, input().split())]



for _ in range(1, 1 + int(input())):
    buf = [g() for _ in range(int(input()))]
    px, py, dmin = 0, 0, 1e10
    for p in buf:
        x1, y1, x2, y2 = p
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                d = 0
                for q in buf:
                    a1, b1, a2, b2 = q
                    if a1 <= x <= a2:
                        d += (x - a1) * (x - a1 + 1) * (b2 - b1 + 1) // 2
                        d += (a2 - x) * (a2 - x + 1) * (b2 - b1 + 1) // 2
                    else:
                        d += abs(2 * x - (a1 + a2)) * (a2 - a1 + 1) * (b2 - b1 + 1) // 2
                    
                    if b1 <= y <= b2:
                        d += (y - b1) * (y - b1 + 1) * (a2 - a1 + 1) // 2
                        d += (b2 - y) * (b2 - y + 1) * (a2 - a1 + 1) // 2
                    else:
                        d += abs(2 * y - (b1 + b2)) * (b2 - b1 + 1) * (a2 - a1 + 1) // 2
                        
                if d < dmin or (d == dmin and (x < px or (x == px and y < py))):
                    dmin = d
                    px, py = x, y
    print(f'Case #{_}:', px, py, dmin)