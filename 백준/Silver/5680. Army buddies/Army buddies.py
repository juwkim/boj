import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
while sum(l:= g()):
    S, B = l
    buf = [[i - 1, i + 1] for i in range(S + 2)]
    for _ in range(B):
        a, b = g()
        print(buf[a][0] if buf[a][0] != 0 else '*', end=' ')
        print(buf[b][1] if buf[b][1] != S + 1 else '*')
        buf[buf[b][1]][0] = buf[a][0]
        buf[buf[a][0]][1] = buf[b][1]
    print('-')