import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    l, n = g()
    pos = [int(input()) for _ in range(n)]
    Min = 0
    for i in range(n):
        Min = max(Min, min(pos[i], l - pos[i]))
    print(Min, max(l - min(pos), max(pos)))