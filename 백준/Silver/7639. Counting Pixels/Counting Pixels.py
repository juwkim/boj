from math import isqrt

for l in [*open(0)][:-1]:
    _, _, r = map(int, l.split())
    cnt = 0
    for x in range(r):
        cnt += (isqrt(r**2 - x**2 - 1) + 1) * 4
    print(cnt)