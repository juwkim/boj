xs, ys = zip(*[[*map(int, input().split())] for _ in range(3)])
mx, my = sorted(xs)[1], sorted(ys)[1]
segments = []
for x, y in zip(xs, ys):
    if x != mx:
        segments.append((x, y, mx, y))
    if y != my:
        segments.append((mx, y, mx, my))
print(len(segments))
for l in segments:
    print(*l)