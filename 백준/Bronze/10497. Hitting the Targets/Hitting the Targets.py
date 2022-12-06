m = int(input())
p = [input().split() for _ in range(m)]
p = [[p[i][0]] + [*map(int, p[i][1:])] for i in range(m)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    count = 0
    for target in p:
        if target[0][0] == 'r':
            _, x1, y1, x2, y2 = target
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
        if target[0][0] == 'c':
            _, x1, y1, r = target
            if (x - x1)**2 + (y - y1)**2 <= r**2:
                count += 1
    print(count)