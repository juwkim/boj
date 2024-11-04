from math import dist

def P3(x, y, z):
    x, y, z = sorted((x, y, z))
    if x == 0:
        if y > z:
            return dist((y, z), (200, 100))
        return dist((y, z), (100, 200))
    return dist((x, y, z), (100, 100, 100))