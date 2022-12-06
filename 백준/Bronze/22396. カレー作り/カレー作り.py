import math
while (s:= input())[0] != '0':
    R0, W0, C, R = map(int, s.split())
    print(max(0, math.ceil((W0 * C - R0) / R)))