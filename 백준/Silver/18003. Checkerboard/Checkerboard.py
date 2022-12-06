from itertools import cycle
r, c, v, h = map(int, input().split())
rows = [int(input()) for _ in range(v)]
cols = [int(input()) for _ in range(h)]
a = ''.join([x * y for x, y in zip(cols, cycle('BW'))])
b = ''.join([x * y for x, y in zip(cols, cycle('WB'))])

for x, y in zip(rows, cycle([a, b])):
    for _ in range(x):
        print(y)