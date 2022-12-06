import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

R, C, E, N = g()
Map = [g() for _ in range(R)]
for _ in range(N):
    a, b, d = g()
    
    Max = 0
    for i in range(a-1, a+2):
        for j in range(b-1, b+2):
            Max = max(Max, Map[i][j])
    Max -= d
    for i in range(a-1, a+2):
        for j in range(b-1, b+2):
            Map[i][j] = min(Max, Map[i][j])

cnt = 0
for i in range(R):
    for j in range(C):
        cnt += max(0, E - Map[i][j])
print(cnt * 72 * 72)