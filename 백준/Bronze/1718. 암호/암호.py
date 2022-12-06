from itertools import cycle
plane = [*map(ord, input())]
key = [*map(lambda x: ord(x) - 96, input())]
print(''.join(map(lambda x: chr(97 + (x[0]-x[1]-97) % 26) if x[0] > 32 else chr(x[0]), zip(plane, cycle(key)))))