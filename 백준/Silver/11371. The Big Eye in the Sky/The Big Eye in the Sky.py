from math import atan, degrees
while (s:= input()) != '0 0':
    x, y = map(int, s.split())
    if x == 0:
        print(90 + 180 * (y < 0))
    else:
        print(round(degrees(atan(y/x))))