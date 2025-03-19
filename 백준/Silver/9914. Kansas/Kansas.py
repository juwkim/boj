import sys
input = sys.stdin.readline

time, x, y = 0, 0, 0
for _ in range(int(input())):
    d, h, s = map(int, input().split())
    match d:
        case 3:
            if y == 0 and x < 0 and x + s * h >= 0:
                time += (-x + s - 1) // s
                break
            time += h
            x += s * h
        case 9:
            if y == 0 and x > 0 and x - s * h <= 0:
                time += (x + s - 1) // s
                break
            time += h
            x -= s * h
        case 12:
            if x == 0 and y < 0 and y + s * h >= 0:
                time += (-y + s - 1) // s
                break
            time += h
            y += s * h
        case 6:
            if x == 0 and y > 0 and y - s * h <= 0:
                time += (y + s - 1) // s
                break
            time += h
            y -= s * h
else:
    print(-1)
    exit(0)
print((time - 1) // 5)