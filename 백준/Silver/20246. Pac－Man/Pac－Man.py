g = lambda: [*map(int, input().split())]


x, y = g()
while x + y:
    print(x, y)
    if x:
        x -= 1
    else:
        y -= 1
    
for i in range(10):
    if i&1:
        for j in range(9, -1, -1):
            print(i, j)
    else:
        for j in range(10):
            print(i, j)