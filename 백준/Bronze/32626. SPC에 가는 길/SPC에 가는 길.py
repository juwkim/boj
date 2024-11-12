SX, SY, EX, EY, PX, PY = map(int, open(0).read().split())
if SX != EX and SY != EY:
    print(1)
elif SX == EX:
    if EX == PX and (SY < PY < EY or EY < PY < SY):
        print(2)
    else:
        print(0)
elif EY == PY and (SX < PX < EX or EX < PX < SX):
    print(2)
else:
    print(0)