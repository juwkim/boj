g = lambda: [*map(int, input().split())]

from itertools import combinations
for i in range(1, 1 + int(input())):
    M = int(input())
    p = g()
    s, e = max(combinations(range(12), 2), key=lambda x: (M // p[x[0]] * (p[x[1]] - p[x[0]]), -p[x[0]]))
    profit = M // p[s] * (p[e] - p[s])
    if profit > 0:   
        print(f'Case #{i}:', s + 1, e + 1, profit)
    else:
        print(f'Case #{i}: IMPOSSIBLE')