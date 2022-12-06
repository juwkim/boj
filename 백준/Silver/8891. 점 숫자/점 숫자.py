g = lambda: [*map(int, input().split())]

dic = {}
x, y = 1, 1
for i in range(1, 50000):
    dic[i] = (x, y)
    dic[(x, y)] = i
    if y == 1:
        x, y = 1, x + y
    else:
        x += 1
        y -= 1
for _ in range(int(input())):
    a, b = g()
    x1, y1 = dic[a]
    x2, y2 = dic[b]
    print(dic[(x1 + x2, y1 + y2)])