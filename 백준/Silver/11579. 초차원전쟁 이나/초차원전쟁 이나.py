import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n = int(input())
    x = [g() for _ in range(n)]
    y = g()
    cnt = 0
    for i in range(n):
        if y[i] == 0:
            continue
        if y[i] < 0 or cnt + y[i] > 2000000000:
            print(0)
            break
        cnt += y[i]
        for j in range(i + 1, n):
            y[j] -= x[i][j] * y[i]
    else:
        print(1, cnt)