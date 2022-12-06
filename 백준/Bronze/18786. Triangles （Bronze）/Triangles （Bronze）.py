from itertools import combinations
g = lambda: [*map(int, input().split())]
def area(a, b, c):
    x1, x2, x3 = a[0], b[0], c[0]
    y1, y2, y3 = a[1], b[1], c[1]
    if len(set([x1, x2, x3])) != 3 and len(set([y1, y2, y3])) != 3:
        res = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    else:
        return 0
    return abs(res)


pos = [g() for _ in range(int(input()))]
print(max(area(a, b, c) for a, b, c in combinations(pos, 3)))