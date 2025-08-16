import sys
from bisect import bisect_left
g = lambda: map(int, sys.stdin.readline().split())

n, m = g()
PA, PB = [0], [0]
for a in g(): PA.append(PA[-1] + a)
for b in g(): PB.append(PB[-1] + b)
for _ in range(int(input())):
    d, m, c = input().split()
    d, m = int(d), int(m)
    l = (PA, PB)[c == 'B']
    if c == 'A':
        cnt = PA[m - 1] + d
        k = bisect_left(PB, cnt)
        day = cnt - PB[k - 1]
    else:
        cnt = PB[m - 1] + d
        k = bisect_left(PA, cnt)
        day = cnt - PA[k - 1]
    print(f"{day} {k}")