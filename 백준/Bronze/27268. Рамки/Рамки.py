def g(): return [*map(int, input().split())]

h, w, n = g()
frame = [['.'] * w for _ in range(h)]
cur = ord('a')
for _ in range(n):
    r1, c1, r2, c2 = g()
    frame[r1 - 1][c1 - 1:c2] = [chr(cur)] * (c2 - c1 + 1)
    frame[r2 - 1][c1 - 1:c2] = [chr(cur)] * (c2 - c1 + 1)
    for i in range(r1, r2 - 1):
        frame[i][c1 - 1] = chr(cur)
        frame[i][c2 - 1] = chr(cur)    
    cur += 1

for line in frame:
    print(*line, sep='')