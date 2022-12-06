import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(i, j):
    global cnt
    if i < 0 or i >= N or j < 0 or j >= N or Map[i][j] == '0':
        return
    Map[i][j] = '0'
    cnt += 1
    for x, y in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
        dfs(x, y)       
N = int(input())
Map = [[*input()] for _ in range(N)]

ans = 0
buf = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == '1':
            cnt = 0
            dfs(i, j)
            buf.append(cnt)
            ans += 1
print(ans, *sorted(buf))