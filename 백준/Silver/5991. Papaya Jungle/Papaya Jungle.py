def g(): return [*map(int, input().split())]
def f(rows): return [g() for _ in range(rows)]

R, C = g()
mat = f(R)
x, y = 0, 0
ans = 0
visited = [bytearray(C) for _ in range(R)]
while True:
    ans += mat[x][y]
    visited[x][y] = True
    
    if x == R - 1 and y == C - 1:
        break
    
    i, j = None, None
    for p, q in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= p < R and 0 <= q < C and visited[p][q] == False:
            if i == None or mat[i][j] < mat[p][q]:
                i, j = p, q
    x, y = i, j
print(ans)