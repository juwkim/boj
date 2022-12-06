while n:= int(input()):
    Map = [input().replace('.', ' ') for _ in range(n)]
    Map += [''.join(l) for l in zip(*Map)]
    for line in Map:
        buf = [len(s) for s in line.split()]
        if buf:
            print(*buf)
        else:
            print(0)