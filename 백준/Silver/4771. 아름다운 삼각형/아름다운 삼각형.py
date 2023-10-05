import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import dist, sqrt, acos, degrees

def angle(a1, a2, b1, b2):
    return degrees(acos((a1 * b1 + a2 * b2) / (sqrt(a1 ** 2 + a2 ** 2) * sqrt(b1 ** 2 + b2 ** 2))))
e = 1e-2
while True:
    s = input()
    if s == '-1':
        break
    x1, y1, x2, y2, x3, y3 = map(float, s.split())
    x1, x2, x3 = x1 - x3, x2 - x3, x3 - x3
    y1, y2, y3 = y1 - y3, y2 - y3, y3 - y3
    d1 = dist((x1, y1), (x2, y2))
    d2 = dist((x2, y2), (x3, y3))
    d3 = dist((x3, y3), (x1, y1))
    d1, d2, d3 = sorted([d1, d2, d3])
    if d1 + d2 <= d3:
        print("Not a Triangle")
        continue
    ans = []
    if d3 - d1 <= 1e-2:
        ans.append("Equilateral")
    elif d2 - d1 <= 1e-2 or d3 - d2 <= 1e-2:
        ans.append("Isosceles")
    else:
        ans.append("Scalene")
    a = angle(x1, y1, x2, y2)
    b = angle(-x2, -y2, x1 - x2, y1 -y2)
    c = angle(-x1, -y1, x2 - x1, y2 - y1)
    if any(88 < i < 92 for i in [a, b, c]):
        ans.append("Right")
    elif any(i >= 92 for i in [a, b, c]):
        ans.append("Obtuse")
    else:
        ans.append("Acute")
    # print(a2.sqrt(), b2.sqrt(), c2.sqrt())
    # print(a2, b2, c2)
    print(*ans)