import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
title = []
for _ in range(N):
    name, score = input().split()
    title.append((name, int(score)))

for _ in range(M):
    num = int(input())
    l, r = -1, N - 1
    while l + 1 < r:
        m = (l + r) // 2
        if num <= title[m][1]:
            r = m
        else:
            l = m
    print(title[r][0])