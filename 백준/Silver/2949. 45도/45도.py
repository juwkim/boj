g = lambda: [*map(int, input().split())]


R, C = g()
Map = [input() for _ in range(R)]
angle_r, angle_q = divmod(int(input()), 90)
if angle_r == 1:
    Map = [l[::-1] for l in zip(*Map)]
elif angle_r == 2:
    Map = [l[::-1] for l in Map[::-1]]
elif angle_r == 3:
    Map = [*zip(*Map)][::-1]
if angle_q == 0:
    for line in Map:
        print(*line, sep='')
else:
    space = len(Map) - 1
    
    p_min = -1
    q_max = len(Map[0])
    
    for i in range(space):
        buf = [' ' * (space - i - 1)]
        
        p, q = i, 0
        while p != -1 and q != q_max:
            buf.append(Map[p][q])
            p -= 1
            q += 1
        print(*buf, sep=' ')
    
    for j in range(q_max):
        buf = []
        if j:
            buf.append(' ' * (j - 1))
        
        p, q = space, j
        while p != -1 and q != q_max:
            buf.append(Map[p][q])
            p -= 1
            q += 1
        print(*buf, sep=' ')