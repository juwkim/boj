g = lambda: [*map(int, input().split())][1:]
while N:= int(input()):
    dic = {i: set(g()) for i in range(1, 1 + N)}
    l = set(g())
    buf = [i for i in range(1, 1 + N) if l.issubset(dic[i])]
    print(buf[0] if len(buf) == 1 else -1)