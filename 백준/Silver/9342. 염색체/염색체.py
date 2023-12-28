import re

l = re.compile(r'^[ABCDEF]?A+F+C+[ABCDEF]?$')
for _ in range(int(input())):
    print('Infected!' if l.match(input()) else 'Good')