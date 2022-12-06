import sys
from itertools import chain
from collections import Counter
I = sys.stdin.readline

N, M, B = map(int, I().split())
field = Counter(chain(*[[*map(int, I().split())] for _ in range(N)]))
s, t = field.items(), field.keys()
a, b = min(t), max(t)
min_time, floor = 999999999, 0
for i in range(b, a - 1, -1):
    top = sum((height - i) * count for height, count in s if height - i > 0)
    bot = sum((i - height) * count for height, count in s if i - height > 0)
    if top + B >= bot:
        time = top * 2 + bot
        if time < min_time:
            min_time = time
            floor = i
print(min_time, floor)