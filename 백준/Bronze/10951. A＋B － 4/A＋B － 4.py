while(True):
    try:
        points = list(map(int, input().split()))
        print(points[0] + points[1])
    except:
        break