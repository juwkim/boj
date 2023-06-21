for _ in range(int(input())):
    m = bin(int(input()))[-1:1:-1]
    x = m.find('1')
    y = m.find('1', x + 1)
    if y == -1:
        print(x - 1, x - 1)
    else:
        print(x, y)