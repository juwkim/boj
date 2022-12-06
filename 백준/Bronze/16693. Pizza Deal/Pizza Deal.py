from math import pi
A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())
print(['Slice of','Whole'][A1/P1 < pi * R1**2 / P2], 'pizza')