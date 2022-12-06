import sys
num = 1
for line in sys.stdin:
    diameter, rotation, time = map(float, line.split())
    if rotation == 0:
        break
    distance = 3.1415927 * diameter * rotation / 5280 / 12
    MPH = distance / time * 3600
    print('Trip #%d: %.2f %.2f' % (num, distance, MPH))
    num += 1