import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]


N = int(input())
d = [[1e9] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(int(input())):
    a, b, c = g()
    d[a - 1][b - 1] = min(d[a - 1][b - 1], c)
    
for m in range(N):
    for s in range(N):
        for e in range(N):
            if d[s][e] > d[s][m] + d[m][e]:
                d[s][e] = d[s][m] + d[m][e]
for line in d:
    for num in line:
        print(0 if num == 1e9 else num, end=' ')
    print()