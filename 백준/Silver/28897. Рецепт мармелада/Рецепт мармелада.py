n, m, *b = map(int, open(0).read().split())
prv = 0
for i, cur in enumerate(b, 1):
    for _ in range(cur - prv):
        print(i, end=' ')
    prv = cur