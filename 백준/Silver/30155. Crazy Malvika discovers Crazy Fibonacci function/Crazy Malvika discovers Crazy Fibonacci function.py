for _ in range(int(input())):
    A, B, N = map(int, input().split())
    mod = 10 ** 9 + 7
    for _ in range((N - 1) % 6):
        A, B = B % mod, B - A
    print(A % mod)