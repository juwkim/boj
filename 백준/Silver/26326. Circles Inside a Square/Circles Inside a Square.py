from math import cos, pi

c = 4 * (1 + 2 * cos(pi / 12))**2
for _ in range(int(input())):
    print("%.5f" % (c * float(input())**2))