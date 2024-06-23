import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
a = [0] * N
for _ in range(M):
    cmd, i, *x = g()
    i -= 1
    match cmd:
        case 1:
            a[i] |= 1 << (x[0] - 1)
        case 2:
            a[i] &= ~(1 << (x[0] - 1))
        case 3:
            a[i] = a[i] << 1 & (1 << 20) - 1
        case 4:
            a[i] = a[i] >> 1
print(len({*a}))