g = lambda: [*map(int, input().split())]
while (s:= input()) != '0 0':
    B, N = map(int, s.split())
    R = g()
    for _ in range(N):
        D, C, V = g()
        R[D-1] -= V
        R[C-1] += V
    print('S' if all(bank >= 0 for bank in R) else 'N')