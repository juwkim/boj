g = lambda: [*map(int, input().split())]

from math import dist
for _ in range(int(input())):
    S, H = g()
    
    ans = False
    hatchs = set(tuple(g()) for _ in range(H))
        
    for x in range(1, S):
        for y in range(1, S):
            if (x, y) not in hatchs:
                d = min(x, S - x, y, S - y)
                if all(dist((x, y), hatch) <= d for hatch in hatchs):
                    ans = x, y
                    break
        if ans:
            break
    
    if ans:
        print(*ans)
    else:
        print(-1, -1)