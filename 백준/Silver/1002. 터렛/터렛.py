import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

T = int(input())

for _ in range(T):
    points = list(map(int, input().split()))
    
    dist1 = dist(points[0], points[1], points[3], points[4])
    dist2 = points[2] + points[5]
    diff = abs(points[2] - points[5])
    
    if (points[0] == points[3]) and (points[1] == points[4]):
        if points[2] == points[5]:
            print(-1)
        else:
            print(0)
    elif dist2 < dist1:
        print(0)
    elif dist1 == dist2:
        print(1)
    elif diff < dist1 < dist2:
        print(2)
    elif diff == dist1:
        print(1)
    else:
        print(0)