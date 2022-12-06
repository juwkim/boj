g = lambda: [*map(int, input().split())]
while sum(l:= g()):
    N, M = l
    buf = [g() for _ in range(M)]
    buf.sort(key=lambda x: x[0])
    infected = bytearray(N+1)
    infected[1] = 1
    for _, s, d in buf:
        if infected[s]:
            infected[d] = 1
    print(sum(infected))