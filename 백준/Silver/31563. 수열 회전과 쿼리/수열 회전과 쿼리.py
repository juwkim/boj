import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, Q = g()
px = [0] * (N + 1)
for i, num in enumerate(g()):
    px[i + 1] = px[i] + num
s = 0
for _ in range(Q):
    cmd, *arg = g()
    match cmd:
        case 1:
            s = (s - arg[0]) % N
        case 2:
            s = (s + arg[0]) % N
        case 3:
            a, b = arg
            if s + b - 1 < N:
                print(px[s + b] - px[s + a - 1])
            elif s + a - 1 >= N:
                print(px[s + b - N] - px[s + a - 1 - N])
            else:
                print(px[N] - px[s + a - 1] + px[s + b - N])