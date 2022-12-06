g = lambda: [*map(int, input().split())]


C, R = g()
K = int(input())
if K > C * R:
    print(0)
else:
    Map = [[1] * (C + 2)] + [[1] + [0] * C + [1] for _ in range(R)] + [[1] * (C + 2)] 
    x, y, d = 1, 1, 0
    for _ in range(K-1):
        Map[x][y] = 1
        if d == 0:
            if Map[x+1][y]:
                y += 1
                d = 1
            else:
                x += 1
        elif d == 1:
            if Map[x][y+1]:
                x -= 1
                d = 2
            else:
                y += 1
        elif d == 2:
            if Map[x-1][y]:
                y -= 1
                d = 3
            else:
                x -= 1
        else:
            if Map[x][y-1]:
                x += 1
                d = 0
            else:
                y -= 1
    
    print(y, x)