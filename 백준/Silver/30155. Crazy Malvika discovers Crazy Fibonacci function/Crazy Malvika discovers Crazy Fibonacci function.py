N, *l = open(0)
for s in l:
    A, B, N = map(int, s.split())
    mod = 10 ** 9 + 7
    for _ in range((N - 1) % 6):
        A, B = B % mod, B - A
    print(A % mod)