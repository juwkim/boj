import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
b, c = bytearray(N + 1), N
for _ in range(Q):
    cmd, *l = g()
    if cmd == 3:
        print(c)
    else:
        x = l[0]
        if cmd == 1:
            c -= b[x] == 0
            b[x] = 1
        else:
            c += b[x] == 1
            b[x] = 0