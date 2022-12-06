from collections import defaultdict

for _ in range(int(input())):
    res = defaultdict(int)
    for _ in range(16):
        t1, t2, g1, g2 = input().split()
        if int(g1) > int(g2):
            res[t1] += 1
        else:
            res[t2] += 1
    print(max(res.items(), key= lambda x: x[1])[0])