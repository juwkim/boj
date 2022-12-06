g = lambda: [*map(int, input().split())]

N, M = g()
lights = [0 for _ in range(N)]
for _ in range(M):
    op, s, e = g()
    if op == 0:
        for i in range(s-1, e):
            lights[i] ^= 1
    else:
        print(sum(lights[s-1:e]))