from math import dist, sqrt, acos, degrees

def angle(x):
    return degrees(acos(((x - x1) * (x - x2) + y1 * y2) / (dist((x, 0), (x1, y1)) * dist((x, 0), (x2, y2)))))

for tc in range(1, 1 + int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if y1 == y2:
        x = (x1 + x2) / 2
        theta = angle(x)
    else:
        sq = dist((x1, y1), (x2, y2)) * sqrt(y1 * y2)
        l = (-x2 * y1 + x1 * y2 - sq) / (y2 - y1)
        r = (-x2 * y1 + x1 * y2 + sq) / (y2 - y1)
        theta = max(angle(l), angle(r))
    print(f'Case #{tc}:', theta)