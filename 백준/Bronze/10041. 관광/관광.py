g = lambda: [*map(int, input().split())]
W, H, N = g()
trip, dist = [g() for _ in [0]*N], 0
for s,e in zip(trip, trip[1:]):
    if all(x <= y for x,y in zip(s,e)) or all(x >= y for x,y in zip(s,e)):
        dist += max(abs(e[0]-s[0]), abs(e[1]-s[1]))
    else:
        dist += abs(e[0]-s[0]) + abs(e[1]-s[1])
print(dist)