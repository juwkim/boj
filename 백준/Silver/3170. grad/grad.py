g = lambda: [*map(int, input().split())]

def dist2(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

X, Y = g()
N = int(input())
cranes = [g() for _ in range(N)] + [(X >> 1, 0, 0)]
reachable = set()
visited = bytearray(N + 1)
visited[N] = True
st = [(X >> 1, 0, 0)]
while st:
    x1, y1, r1 = st.pop()
    for i, (x2, y2, r2) in enumerate(cranes):
        if not visited[i] and dist2(x1, y1, x2, y2) <= (r1 + r2)**2:
            visited[i] = True
            reachable.add((x2, y2, r2))
            st.append((x2, y2, r2))
for _ in range(int(input())):
    D, E = g()
    if any(dist2(cx, cy, D, E) <= r * r for cx, cy, r in reachable):
        print("DA")
    else:
        print("NE")