g = lambda: [*map(int, input().split())]

for i in range(1, 1 + int(input())):
    n, d, f, l = g()
    tmp = n
    n %= d
    buf = []
    for _ in range(l+1):
        p, n = divmod(n * 7, d)
        buf.append(str(p))
    print(f'Problem set {i}: {tmp} / {d}, base 7 digits {f} through {l}:', ''.join(buf[f:l+1]))