g = lambda: [*map(int, input().split())]
from collections import defaultdict

while (l:=g()) != [0]:
    dic = [defaultdict(lambda: -1) for _ in range(4)]
    for _ in range(l[1]):
        k, x, y, s, t = g()
        for _ in range(k):
            for i, j in enumerate((x, y, x + y, x - y)):
                dic[i][j] += 1
            x, y = x + s, y + t
    print(sum(sum(d.values()) for d in dic))