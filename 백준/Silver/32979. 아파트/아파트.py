import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N2 = 2 * int(input())
input()
a = g()
cur = 0
for b in g():
    cur = (cur + b - 1) % N2
    print(a[cur], end=' ')