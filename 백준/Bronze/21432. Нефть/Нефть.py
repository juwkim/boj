g = lambda: [*map(int, input().split())]

n, a, b = g()
costs = [g() for _ in range(n)]

if n == 1:
    print('%.2f' % max(a / costs[0][0], b / costs[0][1]))
else:
    tmp = costs.copy()
    p = tmp.pop(tmp.index(min(tmp, key=lambda x: (x[0], -x[1]))))[0]
    q = min(tmp, key=lambda x: x[1])[1]
    ans1 = a / p + b / q
    
    tmp = costs
    p = tmp.pop(tmp.index(min(tmp, key=lambda x: (x[1], -x[0]))))[1]
    q = min(tmp)[0]
    ans2 = a / q + b / p
    print('%.2f' % max(ans1, ans2))