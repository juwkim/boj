g = lambda: [*map(int, input().split())]

N, a, b, c, d, e, f, g, h, M = g()
buf = []
for i in range(3*N):
    U = (e * pow(i, 5, h) + f * pow(i, 3, h) + g) % h
    W = (a * pow(i, 5, d) + b * pow(i, 2, d) + c) % d
    buf.append((U, W))

buf.sort(key=lambda x: (-x[0], x[1]))
ans = sum(buf[i][1] for i in range(N)) % M
print(ans)