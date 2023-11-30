import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
while N:
    h = 0
    cur = 1
    while cur <= N:
        h += 1
        N -= cur
        cur += 1
    print(h)