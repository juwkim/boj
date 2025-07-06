import sys
g = lambda: map(int, sys.stdin.readline().split())
from collections import Counter

N, M = g()
for _ in range(M):
    cnt = Counter(g())
    if cnt[1] or cnt[2]:
        if cnt[-1] or cnt[-2] % 2 == 0:
            print(1 << cnt[2] + cnt[-2])
        else:
            print(1 << cnt[2] + cnt[-2] - 1)
    elif cnt[-1] + cnt[-2] == 0:
        print(0)
    elif cnt[-1] + cnt[-2] == 1:
        if cnt[0]:
            print(0)
        elif cnt[-1]:
            print(-1)
        else:
            print(-2)
    elif cnt[-1] or cnt[-2] % 2 == 0:
        print(1 << cnt[-2])
    else:
        print(1 << cnt[-2] - 1)