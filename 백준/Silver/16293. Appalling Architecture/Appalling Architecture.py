g = lambda: map(int, input().split())

h, w = g()
Map = [input() for _ in range(h)]
Sum, cnt = 0, 0
x1, x2 = None, None
for idx, line in enumerate(zip(*Map)):
    w = h - line.count('.')
    if w:
        cnt += w
        Sum += idx * w
        if line[-1] != '.':
            if x1 == None:
                x1 = idx
            x2 = idx

center = Sum / cnt
if center < x1 - 0.5:
    print('left')
elif center > x2 + 0.5:
    print('right')
else:
    print('balanced')