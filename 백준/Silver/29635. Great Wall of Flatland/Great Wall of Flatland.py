from collections import Counter
from math import dist

def key(x1, y1, x2, y2):
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    return x1, y1, x2, y2

edges = []
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    edges.extend((key(x1, y1, x2, y2), key(x2, y2, x3, y3), key(x3, y3, x1, y1)))
cnt = Counter(edges)
print(sum(dist((x1, y1), (x2, y2)) for (x1, y1, x2, y2), cnt in cnt.items() if cnt == 1))