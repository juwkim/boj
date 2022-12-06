g = lambda: [*map(int, input().split())]
while int(input()):
    A, B = 0, 0
    for x, y in zip(g(), g()):
        if x > y + 1:
            A += x
        elif y > x + 1:
            B += y
        elif x == y + 1:
            if y == 1:
                B += 6
            else:
                B += x + y
        elif y == x + 1:
            if x == 1:
                A += 6
            else:
                A += x + y
    print(f'A has {A} points. B has {B} points.\n')