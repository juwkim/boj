while (s:= input()) != '0 0 0 0':
    x1, y1, x2, y2 = map(int, s.split())
    if x1 == x2 and y1 == y2:
        print(0)
    elif x1 == x2 or y1 == y2 or x2 - x1 == y2 - y1 or x1 + y1 == x2 + y2:
        print(1)
    else:
        print(2)