import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if (x1 - x2) * (y3 - y4) == (y1 - y2) * (x3 - x4):
        if x1 == x2:
            if x1 == x3:
                print("LINE")
            else:
                print("NONE")
        else:
            a = (y1 - y2) * -x1 / (x1 - x2) + y1
            b = (y3 - y4) * -x3 / (x3 - x4) + y3
            if a == b:
                print("LINE")
            else:
                print("NONE")
    else:
        x = ((y3 - y1) * (x1 - x2) * (x3 - x4) + x1 * (y1 - y2) * (x3 - x4) - x3 * (y3 - y4) * (x1 - x2)) / ((y1 - y2) * (x3 - x4) - (y3 - y4) * (x1 - x2))
        if x1 == x2:
            y = (y3 - y4) * (x - x3) / (x3 - x4) + y3
        else:
            y = (y1 - y2) * (x - x1) / (x1 - x2) + y1
        print(f"POINT {x:.2f} {y:.2f}")