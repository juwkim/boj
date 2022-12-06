g = lambda: [*map(int, input().split())]

import sys
input = lambda: sys.stdin.readline().rstrip('\n')

for cnt in range(1, 1 + int(input())):
    ans = 0
    n = int(input())
    s, f = g()
    for _ in range(n):
        si, fi, r = g()
        ans += r * max(min(f, fi) - max(s, si) + 1, 0)
    print(f'Data Set {cnt}:\n{ans}\n')