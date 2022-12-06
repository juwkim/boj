while(True):
    points = list(map(int, input().split()))
    plus = points[0] + points[1]
    if plus != 0:
        print(points[0] + points[1])
    else:
        break