from math import gcd
def P1(x1, y1, x2, y2, x3, y3):
    return gcd(x1 - x2, y1 - y2) + gcd(x2 - x3, y2 - y3) + gcd(x3 - x1, y3 - y1)