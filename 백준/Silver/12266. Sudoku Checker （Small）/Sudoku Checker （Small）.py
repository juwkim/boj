g = lambda: [*map(int, input().split())]
for step in range(1, 1 + int(input())):
    N = int(input())
    buf = [g() for _ in range(N * N)]
    buf += [*zip(*buf)]
    for i in range(0, N * N, N):
        for j in range(0, N * N, N):
            l = sum([buf[k][j:j+N] for k in range(i, i + N)], [])
            buf.append(l)
    cmp = [*range(1, N * N + 1)]
    if all(cmp == line for line in map(sorted, buf)):
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'Case #{step}: {ans}')