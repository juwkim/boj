g = lambda: [*map(int, input().split())]
while True:
    try:
        N, M = g()
        Map = [g() for _ in range(N)]
        
        
        x, y = None, None
        MTX = None
        Min = 1e10
        for i in range(N-M+1):
            for j in range(N-M+1):
                tmp = ''.join(map(str, sorted(set(sum([Map[k][j:j+M] for k in range(i, i+M)], [])), reverse=True)))
                if len(tmp) < Min or (len(tmp) == Min and tmp > MTX):
                    x, y = i + 1, j + 1
                    MTX = tmp
                    Min = len(tmp)
        print(x, y)
    except:
        break