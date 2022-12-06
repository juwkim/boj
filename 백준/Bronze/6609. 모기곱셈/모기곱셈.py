import sys
for line in sys.stdin:
    M, P, L, E, R, S, N = map(int, line.split())
    for _ in range(N):
        M, P, L = P//S, L//R, M*E
    print(M)