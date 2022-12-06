king, rock, N = input().split()
king = ord(king[0]) - 64, int(king[1])
rock = ord(rock[0]) - 64, int(rock[1])

dx = {'B': 0, 'T': 0, 'L': -1, 'R': 1}
dy = {'B': -1, 'T': 1, 'L': 0, 'R': 0}
def move(pos, d):
    x, y = pos
    for i in d:
        x += dx[i]
        y += dy[i]
    if 1 <= x <= 8 and 1 <= y <= 8:
        return x, y
    else:
        return 0, 0
    
for _ in range(int(N)):
    d = input()
    a, b = move(king, d)
    c, d = move(rock, d)
    if a:
        if (a, b) == rock:
            if c:
                king = (a, b)
                rock = (c, d)
        else:
            king = (a, b)

for a, b in (king, rock):
    print(chr(a + 64) + str(b))