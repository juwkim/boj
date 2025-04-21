import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    a = [[*input()] for _ in range(R)]
    x, y = -1, -1
    for i in range(R):
        for j in range(C):
            if a[i][j] != '?':
                x, y = i, j
                break
        if x != -1:
            break
    t = a[x][y]
    for j in range(C):
        if a[x][j] == '?':
            a[x][j] = t
        else:
            t = a[x][j]
    for i in range(x - 1, -1, -1):
        y = 0
        while y < C and a[i][y] == '?':
            y += 1
        if y == C:
            for j in range(C):
                a[i][j] = a[i + 1][j]
        else:
            t = a[i][y]
            for j in range(C):
                if a[i][j] == '?':
                    a[i][j] = t
                else:
                    t = a[i][j]
    for i in range(x + 1, R):
        y = 0
        while y < C and a[i][y] == '?':
            y += 1
        if y == C:
            for j in range(C):
                a[i][j] = a[i - 1][j]
        else:
            t = a[i][y]
            for j in range(C):
                if a[i][j] == '?':
                    a[i][j] = t
                else:
                    t = a[i][j]
    print(f"Case #{tc}:")
    for l in a:
        print(*l, sep='')