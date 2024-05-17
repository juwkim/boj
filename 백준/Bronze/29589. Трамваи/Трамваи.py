import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
trams = [input() for _ in range(n)]
i, capa = 0, 0
for _ in range(m):
    t = input()
    while i < n and t > trams[i]:
        i += 1
        capa = 0
    if i == n:
        print(-1)
    else:
        print(i + 1)
        capa += 1
        if capa == k:
            i += 1
            capa = 0