for _ in range(int(input())):
    a = [*map(int, input().split()[1:])]
    x, y = a[::2], a[1::2]
    s = max(y.count(i) for i in y)
    print(s)