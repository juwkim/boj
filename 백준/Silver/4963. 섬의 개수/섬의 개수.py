g = lambda: [*map(int, input().split())]

def dfs(i, j):
    if Map[i][j]:
        Map[i][j] = 0
        for s in range(max(0, i-1), min(h, i+2)):
            for t in range(max(0, j-1), min(w, j+2)):
                dfs(s, t)

while sum(s:=g()):
    w, h = s
    Map = [g() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if Map[i][j]:
                ans += 1
                dfs(i, j)
    print(ans)