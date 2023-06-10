from statistics import median
g = lambda: [*map(int, input().split())]

w, h = g()
x, y = 0, 0
while (l:=g()) != [0, 0]:
    x = median([0, x + l[0], w])
    y = median([0, y + l[1], h])
    print(x, y)