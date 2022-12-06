from math import dist
g = lambda: [*map(int, input().split())]
i = 1
while (l:= g())[0]:
    r, *p = l
    flag = False    
    while sum(q:= g()) != -2:
        if flag:
            continue
        if dist(p, q) < r + 1:
            flag = True
            print(f'Firefly {i} caught at ({q[0]},{q[1]})')
        v = (q[0] - p[0], q[1] - p[1])
        mul = r / dist(v, (0, 0))
        p[0] += v[0] * mul
        p[1] += v[1] * mul
    if not flag:
        print(f'Firefly {i} not caught')
    i += 1