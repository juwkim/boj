N, K = map(int, input().split())
l = [], [], []
idx = {'s': (0, 1, 2), 'r': (1, 2, 0), 'p': (2, 0, 1)}
for c in input():
    for i in idx[c]:
        if len(l[i]) < K:
            l[i].append(c)
            break
for p in l:
    print(*p, sep='')