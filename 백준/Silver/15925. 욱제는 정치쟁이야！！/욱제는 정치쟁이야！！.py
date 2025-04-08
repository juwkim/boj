import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, C = g()
a = [g() for _ in range(N)]
while True:
    flag = False
    for i in range(N):
        if N < a[i].count(C) * 2 < 2 * N:
            flag = True
            for j in range(N):
                if a[i][j] != C:
                    a[i][j] ^= 1
    for j in range(N):
        if N < sum(a[i][j] == C for i in range(N)) * 2 < 2 * N:
            flag = True
            for i in range(N):
                if a[i][j] != C:
                    a[i][j] ^= 1
    if not flag:
        break
print(+all(all(c == C for c in row) for row in a))