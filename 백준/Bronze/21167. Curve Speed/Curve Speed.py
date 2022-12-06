import sys
for i in sys.stdin:
    R, S = i.split()
    V = ((int(R) * (float(S) + 0.16)) / 0.067)**.5
    print(round(V))