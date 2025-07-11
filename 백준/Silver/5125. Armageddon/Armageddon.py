import math

R = 6378.1
for tc in range(1, int(input()) + 1):
    xa, a_deg, sa, sm = map(float, input().split())
    x = R / math.sin(math.radians(a_deg / 2))
    t = (xa - x) / sa - (x - R) / sm
    print(f"Data Set {tc}:")
    if t < 0:
        print("Oh no!")
    else:
        print(f"{t:.2f}")
    print()