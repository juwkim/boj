A, B, C, X1, X2, Y1, Y2 = map(int, open(0).read().split())
if B:
    P, Q = (-C - A * X1) / B, (-C - A * X2) / B
    if P <= Y1:
        i = Q > Y1
    elif P >= Y2:
        i = Q < Y2
    else:
        i = 1
else:
    i = (A * X1 + C) * (A * X2 + C) < 0
print(("Lucky", "Poor")[i])