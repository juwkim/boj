g = lambda: [*map(int, input().split())]

while True:
    try:
        n, *l = g()
        tmp = sorted(abs(l[i] - l[i+1]) for i in range(n-1))
        if tmp == [*range(1, n)]:
            print('Jolly')
        else:
            print('Not jolly')
    except:
        break