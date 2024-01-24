import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

for _ in range(int(input())):
    C, V = g()
    nums = [g() for _ in range(V)]
    cnt = Counter(l[0] for l in nums)
    if len(cnt) == 1:
        print(cnt.most_common(1)[0][0], 1)
        continue
    (p1, v1), (p2, v2) = cnt.most_common(2)
    if 2 * v1 > V:
        print(p1, 1)
        continue
    a, b = 0, 0
    for l in nums:
        i = l.index(p1)
        j = l.index(p2)
        if i < j:
            a += 1
        else:
            b += 1
    if a > b:
        print(p1, 2)
    else:
        print(p2, 2)