import sys
input = lambda: sys.stdin.readline()

g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    n, m = g()
    buf = [set() for _ in range(n+1)]
    for i in range(m):
        a, b = g()
        buf[a].add(b)
        buf[b].add(a)
    print(f'Data Set {_}:')
    print(*sorted(buf[int(input())]))
    print()