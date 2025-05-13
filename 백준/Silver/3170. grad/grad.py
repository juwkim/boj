g = lambda: [*map(int, input().split())]

def dist2(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

X, Y = g()
N = int(input())
cranes = [g() for _ in range(N)]
cranes.append((X >> 1, 0, 0))
reachable = set()
visited = bytearray(N + 1)
visited[N] = True
st = [N]
while st:
    x1, y1, r1 = cranes[st.pop()]
    for i in range(N):
        if not visited[i]:
            x2, y2, r2 = cranes[i]
            if dist2(x1, y1, x2, y2) <= (r1 + r2)**2:
                visited[i] = True
                reachable.add(i)
                st.append(i)

for _ in range(int(input())):
    D, E = g()
    for i in reachable:
        cx, cy, r = cranes[i]
        if dist2(cx, cy, D, E) <= r * r:
            print("DA")
            break
    else:
        print("NE")