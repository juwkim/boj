from collections import deque
g = lambda: [*map(int, input().split())]

def dist2(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

X, Y = g()
N = int(input())
cranes = [g() for _ in range(N)]

entrance = X // 2, 0
reachable = set()
visited = bytearray(N)
dq = deque()
for i, (cx, cy, r) in enumerate(cranes):
    if dist2(cx, cy, entrance[0], entrance[1]) <= r * r:
        dq.append(i)
        reachable.add(i)
        visited[i] = True
while dq:
    x1, y1, r1 = cranes[dq.popleft()]
    for i, (x2, y2, r2) in enumerate(cranes):
        if not visited[i]:
            if dist2(x1, y1, x2, y2) <= (r1 + r2)**2:
                visited[i] = True
                reachable.add(i)
                dq.append(i)

for _ in range(int(input())):
    D, E = g()
    for i in reachable:
        cx, cy, r = cranes[i]
        if dist2(cx, cy, D, E) <= r * r:
            print("DA")
            break
    else:
        print("NE")