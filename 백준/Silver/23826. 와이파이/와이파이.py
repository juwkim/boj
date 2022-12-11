g = lambda: [*map(int, input().split())]

dist = lambda p, q: abs(p[0] - q[0]) + abs(p[1] - q[1]) 
N = int(input())
*p0, E = g()
rooms = [g() for _ in range(N)]

ans = 0
for i in range(N):
    *pi, _ = rooms[i]
    cur = E - dist(p0, pi)
    
    for j in range(N):
        if cur <= 0:
            break
        *pj, Ej = rooms[j]
        cur -= max(0, Ej - dist(pi, pj))
    ans = max(ans, cur)
if ans == 0:
    ans = 'IMPOSSIBLE'
print(ans)