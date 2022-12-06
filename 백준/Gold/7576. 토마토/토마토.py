import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]


from collections import deque
def bfs():
    qu = deque()
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1:
                qu.append((i, j))
    ret = 0
    while True:
        Next_qu = deque()
        for x, y in qu:
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < N and 0 <= j < M and Map[i][j] == 0:
                    Map[i][j] = 1
                    Next_qu.append((i, j))
        if Next_qu:
            ret += 1
            qu = Next_qu
        else:
            break
    return ret
    
        
        
M, N = g()
Map = [g() for _ in range(N)]
ans = bfs()
if any(0 in line for line in Map):
    print(-1)
else:
    print(ans)