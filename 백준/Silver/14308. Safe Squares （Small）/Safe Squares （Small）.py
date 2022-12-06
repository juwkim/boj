import sys
for step in range(1, 1 + int(sys.stdin.readline())):
    R, C, K = map(int, sys.stdin.readline().split())
    Map = [[0] * (C + 1) for _ in range(R + 1)]
    for _ in range(K):
        r, c = map(int, sys.stdin.readline().split())
        Map[r+1][c+1] = 1
    for i in range(1, 1 + R):
        for j in range(2, 1 + C):
            Map[i][j] += Map[i][j-1]
    for i in range(2, 1 + R):
        for j in range(1, 1 + C):
            Map[i][j] += Map[i-1][j]
    ans = R * C - K
    for size in range(2, 1 + min(R, C)):
        for i in range(R + 1 - size):
            for j in range(C + 1 - size):
                ans += (Map[i+size][j+size] - (Map[i][j+size] + Map[i+size][j]) + Map[i][j] == 0)
    print(f'Case #{step}: {ans}')