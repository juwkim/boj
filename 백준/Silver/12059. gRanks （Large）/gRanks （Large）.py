import sys
input = sys.stdin.readline
from collections import defaultdict

for tc in range(1, 1 + int(input())):
    P = int(input())
    S = [*map(int, input().split())]
    d = defaultdict(list)
    for _ in range(int(input())):
        W, *names = input().split()
        W = int(W)
        for i, name in enumerate(names):
            d[name].append(W * S[i])
    M = int(input())
    l = []
    for name in d:
        l.append((-sum(sorted(d[name], reverse=True)[:M]), name))
    l.sort()
    print(f"Case #{tc}:")
    prv, rank = 0, 0
    for i, (score, name) in enumerate(l, 1):
        if score != prv:
            rank = i
        prv = score
        print(f"{rank}: {name}")