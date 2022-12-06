dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(int(input())):
    maxX, maxY = 0, 0
    minX, minY = 0, 0
    
    x, y, d = 0, 0, 0
    for cmd in input():
        if cmd == 'L':
            d = (d - 1) % 4
        elif cmd == 'R':
            d = (d + 1) % 4
        elif cmd == 'F':
            x += dx[d]
            y += dy[d]
        else:
            x += dx[(d + 2) % 4]
            y += dy[(d + 2) % 4]
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        minX = min(minX, x)
        minY = min(minY, y)
    print((maxX - minX) * (maxY - minY))