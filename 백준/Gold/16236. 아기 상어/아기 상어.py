g = lambda: [*map(int, input().split())]


from collections import deque
N = int(input())
Map = []
x, y = 0, 0
for _ in range(N):
    l = g()
    Map.append(l)
    if 9 in l:
        x, y = _, l.index(9)
        Map[x][y] = 0

size, eat, ans = 2, 0, 0
dq = deque([(x, y, ans)])
visited = [bytearray(N) for _ in range(N)]
pts = None, None
while True:
    while dq:
        x, y, t = dq.popleft()
        visited[x][y] = 1
        for a, b in ((x-1, y), (x, y-1), (x, y+1), (x+1, y)):
            if 0 <= a < N and 0 <= b < N and visited[a][b] == 0 and Map[a][b] <= size:
                visited[a][b] = 1
                if 0 < Map[a][b] < size:
                    if pts == (None, None):
                        pts = (a, b)
                        ans = t+1
                    elif t+1 == ans:
                        if (a, b) < pts:
                            pts = (a, b)
                    else:
                        break
                else:
                    dq.append((a, b, t+1))

    if pts[0] == None:
        break
    a, b = pts
    pts = (None, None)
    dq = deque([(a, b, ans)])
    visited = [bytearray(N) for _ in range(N)]
    
    Map[a][b] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0
print(ans)