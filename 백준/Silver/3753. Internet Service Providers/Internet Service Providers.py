for l in open(0):
    N, C = map(int, l.split())
    print((C + N - 1) // (2 * N) if N else 0)