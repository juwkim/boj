import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

cur = 0
for _ in range(int(input())):
    n, arrival, service, patience = g()
    if cur <= arrival + patience:
        cur = max(cur, arrival) + service
        print(n)