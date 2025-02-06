import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n, l, r = g()
    l -= 1
    a = g()
    print(min(sum(sorted(a[l:])[:r-l]), sum(sorted(a[:r])[:r-l])))