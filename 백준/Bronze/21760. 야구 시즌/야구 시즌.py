for _ in range(int(input())):
    N, M, k, D = map(int, input().split())
    s = M * N * ((k + N) * M - k - M) // 2
    B = int(D / s)
    print(B * s if B else -1)