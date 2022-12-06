g = lambda: [*map(int, input().split())]
R, C = g()
Map = [g() for _ in range(R)]
T = int(input())
ans = 0
for i in range(R - 2):
    for j in range(C - 2):
        buf = Map[i][j:j+3] + Map[i+1][j:j+3] + Map[i+2][j:j+3]
        buf.sort()
        ans += buf[4] >= T
print(ans)