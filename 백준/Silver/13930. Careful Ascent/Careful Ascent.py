g = lambda: [*map(int, input().split())]

        
x, y = g()
dist = y
for _ in range(int(input())):
    l, u, f = input().split()
    l, u = map(int, [l, u])
    dist += (u - l) * (float(f) - 1)
print(x / dist)