from itertools import combinations

for _ in range(int(input())):
    ans, num = None, 0
    l = sorted((a[0], int(a[1:])) for a in input().split())
    for i in 3, 4:
        for c in combinations(l, i):
            if len({x[0] for x in c}) == i and len({x[1] for x in c}) == 1 and i * c[0][1] > num:
                ans, num = c, i * c[0][1]
    for i in range(3, 14):
        for c in combinations(l, i):
            if len({x[0] for x in c}) == 1 and all(c[j][1] + 1 == c[j + 1][1] for j in range(i - 1)) and sum(x[1] for x in c) > num:
                ans, num = c, sum(x[1] for x in c)
    if ans is None:
        print("NO GROUPS OR RUNS")
    else:
        for p in ans:
            print(p[0] + str(p[1]), end=' ')
        print(num)