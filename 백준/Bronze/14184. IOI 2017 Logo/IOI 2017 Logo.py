g = lambda: [*map(int, input().split())]

from collections import defaultdict
while n:= int(input()):
    
    res = [defaultdict(int) for _ in range(3)]
    for _ in range(n):
        d, *l = g()
        for i in range(d):
            res[i][l[i]] += 3 - i
    p = list(set(list(res[0].keys()) + list(res[1].keys()) + list(res[2].keys())))
    winner = []
    s = (0, 0, 0)
    for x in p:
        q = (res[0][x] + res[1][x] + res[2][x], res[0][x], res[1][x])
        if q > s:
            s = q
            winner = [x]
        elif q == s:
            winner.append(x)
    print(*sorted(winner))