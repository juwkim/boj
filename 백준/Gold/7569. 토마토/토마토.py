import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]


from collections import deque
def bfs():
    qu = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if Map[i][j][k] == 1:
                    qu.append((i, j, k))
    ret = 0
    while True:
        Next_qu = deque()
        for x, y, z in qu:
            for i, j, k in ((x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)):
                if 0 <= i < H and 0 <= j < N and 0 <= k < M and Map[i][j][k] == 0:
                    Map[i][j][k] = 1
                    Next_qu.append((i, j, k))
        if Next_qu:
            ret += 1
            qu = Next_qu
        else:
            break
    return ret
    
        
        
M, N, H = g()
Map = [[g() for _ in range(N)] for _ in range(H)]
ans = bfs()
if any(any(0 in line for line in board) for board in Map):
    print(-1)
else:
    print(ans)