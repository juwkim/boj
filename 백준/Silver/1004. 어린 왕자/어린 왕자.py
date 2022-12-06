import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

T = int(input())

for _ in range(T):
    points = list(map(int, input().split()))
    n = int(input())
    total = 0
    for i in range(n):
        check = 0
        planet = list(map(int, input().split()))
        if dist(points[0], points[1], planet[0], planet[1]) > planet[2]:
            check += 1
        if dist(points[2], points[3], planet[0], planet[1]) > planet[2]:
            check += 1
        if check == 1:
            total += 1
    print(total)
            