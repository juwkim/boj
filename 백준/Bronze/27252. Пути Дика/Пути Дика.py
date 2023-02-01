Map = [['.'] * 100 for _ in range(100)]
s, h, max_h = input(), 0, 0
for w, c in enumerate(s):
    if c == '(':
        max_h = max(max_h, h)
        Map[h][w] = '/'
        h += 1
    else:
        h -= 1
        Map[h][w] = '\\'

width = len(s)
for i in range(max_h, -1, -1):
    print(*Map[i][:width], sep='')