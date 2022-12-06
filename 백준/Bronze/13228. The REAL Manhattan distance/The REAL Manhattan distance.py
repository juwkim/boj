for _ in range(int(input())):
    x1, y1, floor1, x2, y2, floor2 = map(int, input().split())
    print(abs(x1-x2)+abs(y1-y2)+floor1+floor2)