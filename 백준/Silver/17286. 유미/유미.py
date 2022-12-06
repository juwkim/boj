from math import dist
g = lambda: [*map(int, input().split())]
a = g()
p = [g() for _ in range(3)]

ans = 1e9
for i in range(3):
    tmp = dist(a, p[i]) + dist(p[i-1], p[i-2])
    tmp += min(dist(p[i], p[i-1]), dist(p[i], p[i-2]))
    ans = min(ans, tmp)
print(int(ans))