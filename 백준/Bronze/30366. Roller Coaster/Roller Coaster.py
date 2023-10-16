import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()

t, cur = 0, 0
for num in g():
    if cur + num <= M:
        cur += num
    else:
        cur = num
        t += 1
    print(t)