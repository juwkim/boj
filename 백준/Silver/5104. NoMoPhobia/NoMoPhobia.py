from collections import defaultdict
def g(): return [*map(int, input().split())]

points = {'TT': 75, 'TX': 50, 'PR': 80, 'RT': 30, 'AP': 25, 'PX': 60}
while (l := g()) != [0, 0]:
    W, N = l
    order = {}
    dic = defaultdict(int)
    for i in range(N):
        name, what = input().split()
        if name not in order:
            order[name] = i
        dic[name] += points[what]
    
    ans = []
    for name in dic:
        if dic[name] >= 100:
            ans.append(name)
    
    ans.sort(key=order.get)
    if ans:
        print(f'Week {W} {",".join(ans)}')
    else:
        print(f'Week {W} No phones confiscated')