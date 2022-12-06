g = lambda: [*map(int, input().split())]

while sum(s:= g()):
    n, m, a = s
    Map = [[-1] * 1000 for _ in range(n)]
    for _ in range(m):
        h, p, q = g()
        Map[p-1][h-1] = q - 1
        Map[q-1][h-1] = p - 1
    cur = a - 1
    for i in range(999, -1, -1):
        if Map[cur][i] != -1:
            cur = Map[cur][i]
    print(cur + 1)