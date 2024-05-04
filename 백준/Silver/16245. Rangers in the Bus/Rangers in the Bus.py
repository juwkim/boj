import sys
g = lambda: map(int, sys.stdin.readline().split())

n, k = g()
red, blue, black, yellow = [], [], [], []
red_pos, blue_pos, black_pos, yellow_pos = 1, 2, 2 * n - 1, 2 * n
seated = set()
for i in range(1, k + 1):
    x, y = g()
    pos = (x - 1) * 2 + y
    seated.add(pos)
    if pos == red_pos:
        red.append(i)
        red_pos += 1
        while red_pos in seated: red_pos += 1
    if pos == blue_pos:
        blue.append(i)
        blue_pos += (-1, 3)[blue_pos & 1]
        while blue_pos in seated: blue_pos += (-1, 3)[blue_pos & 1]
    if pos == black_pos:
        black.append(i)
        black_pos += (-3, 1)[black_pos & 1]
        while black_pos in seated: black_pos += (-3, 1)[black_pos & 1]
    if pos == yellow_pos:
        yellow.append(i)
        yellow_pos += -1
        while yellow_pos in seated: yellow_pos += -1

print(len(red), *red)
print(len(blue), *blue)
print(len(black), *black)
print(len(yellow), *yellow)
print(k, *range(1, k + 1))