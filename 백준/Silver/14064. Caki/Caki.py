n, k, *xs = map(int, open(0).read().split())
Prev = [(i - 1) % n for i in range(n)]
Next = [(i + 1) % n for i in range(n)]
points = [*range(n)]
for x in map(lambda v: v - 1, xs):    
    y = Prev[x]
    points[x] -= 1
    points[y] += 1
    prev_y, next_x = Prev[y], Next[x]
    Prev[x], Prev[y], Next[x], Next[y], Next[prev_y], Prev[next_x] = prev_y, x, y, next_x, x, y
print(*sorted(range(1, n + 1), key=lambda v: points[v - 1])[:min(6, n)])