import sys
input = lambda: sys.stdin.readline().rstrip()
from math import radians, sin, cos, acos

cities = {}
while (line := input()) != "#":
    name, lat, lon = line.split()
    cities[name] = radians(float(lat)), radians(float(lon))

while (line := input()) != "# #":
    A, B = line.split()
    print(f"{A} - {B}")
    if A not in cities or B not in cities:
        print("Unknown\n")
    else:
        phi1, lam1 = cities[A]
        phi2, lam2 = cities[B]
        dist = 6378 * acos(sin(phi1) * sin(phi2) + cos(phi1) * cos(phi2) * cos(lam1 - lam2))
        print(f"{int(dist + .5)} km\n")