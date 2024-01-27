import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    a, *f = MIS(); f.reverse()
    b, *g = MIS(); g.reverse()
    c, *h = MIS(); h.reverse()
    fgh = [0] * (a + b - 1)
    for i, v in enumerate(f):
        for j, w in enumerate(g):
            fgh[i + j] ^= v * w
    for i in range(a + b - c - 1, -1, -1):
        if fgh[i + c - 1]:
            for j, v in enumerate(h):
                fgh[i + j] ^= v
    fgh.reverse()
    idx = fgh.index(1)
    print(a + b - 1 - idx, *fgh[idx:])