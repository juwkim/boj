import sys
input = sys.stdin.readline
from datetime import datetime

N = int(input())
if N:
    ds, ls = [], []
    for _ in range(N):
        day, time, l = input().split()
        ds.append(datetime(*map(int, day.split('/')), *map(int, time.split(':'))))
        ls.append(int(l))
    ps = []
    num = 365 * 24 * 60 * 60
    for i in range(N):
        delta = ds[-1] - ds[i]
        ps.append(max(0.5 ** (delta.total_seconds() / num), 0.9 ** (N - 1 - i)))
    X = sum(p * l for p, l in zip(ps, ls)) / sum(ps)
    print(X)
else: 
    print(0)