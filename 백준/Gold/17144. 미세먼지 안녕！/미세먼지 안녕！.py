input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def diffuse(Map, R, C, idx):
    
    new_map = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):

            if Map[i][j] == -1:
                new_map[i][j] = -1
                continue

            cnt = 0
            amount = Map[i][j] // 5
            if i > 0 and (i - 1, j) != (idx + 1, 0):
                new_map[i - 1][j] += amount
                cnt += 1
            if j > 0 and (i, j - 1) not in ((idx, 0), (idx + 1, 0)):
                new_map[i][j - 1] += amount
                cnt += 1
            if i < R - 1 and (i + 1, j) != (idx, 0):
                new_map[i + 1][j] += amount
                cnt += 1
            if j < C - 1:
                new_map[i][j + 1] += amount
                cnt += 1
            new_map[i][j] += Map[i][j] - amount * cnt
    return new_map

def move(Map, R, C, idx):

    # up left
    for i in range(idx - 1, 0, -1):
        Map[i][0] = Map[i-1][0]
    
    # up top
    for i in range(C - 1):
        Map[0][i] = Map[0][i + 1]
    
    # up right
    for i in range(idx):
        Map[i][-1] = Map[i + 1][-1]
    
    # up btm
    for i in range(C - 1, 1, -1):
        Map[idx][i] = Map[idx][i - 1]

    # down left
    for i in range(idx + 2, R - 1):
        Map[i][0] = Map[i + 1][0]
    
    # down btm
    for i in range(C - 1):
        Map[-1][i] = Map[-1][i + 1]
    
    # down right
    for i in range(R - 1, idx + 1, -1):
        Map[i][-1] = Map[i - 1][-1]
    
    # down top
    for i in range(C - 1, 1, -1):
        Map[idx + 1][i] = Map[idx + 1][i - 1]

    # cleaned
    Map[idx][1], Map[idx + 1][1] = 0, 0

R, C, T = g()
Map = [g() for _ in range(R)]
idx = 2
while Map[idx][0] != -1:
    idx += 1
    
for _ in range(T):
    Map = diffuse(Map, R, C, idx)
    move(Map, R, C, idx)

print(sum(sum(line) for line in Map) + 2)