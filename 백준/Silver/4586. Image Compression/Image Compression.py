import sys
input = lambda: sys.stdin.readline().rstrip()

def fill(out, x, y, size, color):
    for i in range(x, x + size):
        for j in range(y, y + size):
            out[i][j] = color

def compress(image, out, x, y, size, threshold):
    cnt = {'0': 0, '1': 0}
    for i in range(x, x + size):
        for j in range(y, y + size):
            cnt[image[i][j]] += 1
    total = size * size
    for color in '01':
        if cnt[color] * 100 >= threshold * total:
            fill(out, x, y, size, color)
            return
    half = size >> 1
    compress(image, out, x, y + half, half, threshold)
    compress(image, out, x, y, half, threshold)
    compress(image, out, x + half, y, half, threshold)
    compress(image, out, x + half, y + half, half, threshold)

tc = 1
while (line:=input()) != '0':
    W, T = map(int, line.split())
    image = [input() for _ in range(W)]
    out = [['' for _ in range(W)] for _ in range(W)]
    compress(image, out, 0, 0, W, T)
    print(f"Image {tc}:")
    for row in out:
        print(*row, sep='')
    tc += 1