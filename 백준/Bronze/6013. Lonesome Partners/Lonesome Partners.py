from itertools import combinations  
p = [input() for _ in range(int(input()))]
max_dist = 0
for pp in combinations(p, 2):
    a, b = map(lambda s: [*map(int, s.split())] ,pp)
    dist = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**.5
    if dist > max_dist:
        max_dist = dist
        x, y = pp[0], pp[1]
print(p.index(x)+1, p.index(y)+1)