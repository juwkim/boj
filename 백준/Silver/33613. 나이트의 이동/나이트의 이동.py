N, R, C = map(int, open(0).read().split())
if N == 3:
    if (R, C) == (2, 2):
        print(1)
    else:
        print(4)
else:
    print(N * N // 2 + (N & 1 and (R + C) % 2 == 0))