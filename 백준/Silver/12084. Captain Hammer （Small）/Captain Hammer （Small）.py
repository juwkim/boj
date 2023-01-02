import math
def distance(theta, v):
    # Calculate the distance traveled given the angle of takeoff and the takeoff speed
    return v**2 * math.sin(2*theta) / 9.8


for t in range(1, 1 + int(input())):
    # Read V and D
    v, d = map(int, input().split())

    # Set lower and upper bounds for binary search
    low = 0
    high = math.pi/4

    # Perform binary search
    while high - low > 1e-13:
        mid = (low + high) / 2
        dist = distance(mid, v)
        if dist < d:
            low = mid
        else:
            high = mid

    # Calculate the angle of takeoff in degrees and print result
    theta = (low + high) / 2
    print(f"Case #{t}: {math.degrees(theta)}")