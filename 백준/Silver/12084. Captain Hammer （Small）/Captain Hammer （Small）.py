import math
def distance(theta, v):
    # Calculate the distance traveled given the angle of takeoff and the takeoff speed
    return v**2 * math.sin(2*theta) / 9.8


for t in range(1, 1 + int(input())):
    v, d = map(int, input().split())

    low = 0
    high = math.pi/4

    while high - low > 1e-13:
        mid = (low + high) / 2
        dist = distance(mid, v)
        if dist < d:
            low = mid
        else:
            high = mid

    theta = (low + high) / 2
    print(f"Case #{t}: {math.degrees(theta)}")