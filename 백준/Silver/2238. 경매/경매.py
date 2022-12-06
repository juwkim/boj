import sys
input = lambda: sys.stdin.readline().rstrip('\n')
g = lambda: [*map(int, input().split())]
U, N = g()
money = [0] * (U + 1)
buf = []
for _ in range(N):
    S, P = input().split()
    P = int(P)
    money[P] += 1
    buf.append((S, P))
Min = money.index(min([i for i in money if i]))
for i in range(N):
    if buf[i][1] == Min:
        print(buf[i][0], Min)
        break