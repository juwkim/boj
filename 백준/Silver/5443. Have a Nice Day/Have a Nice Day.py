import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter
for _ in range(int(input())):
    s = input()
    cnt = Counter(s)
    del cnt[' ']
    if len(set(cnt.values())) != 1:
        print('no')
        continue
    D, M, Y = map(int, s.split())
    a, b, c, d = sorted([D, M, *divmod(Y, 100)])
    if a + d == b + c or a + b + c == d:
        print('yes')
    else:
        print('no')