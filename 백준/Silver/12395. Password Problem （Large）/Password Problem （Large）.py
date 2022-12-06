for i in range(1, 1 + int(input())):
    A, B = map(int, input().split())
    s, t = A + 2 * B + 2, B + 1
    m, n = B + 2, 1
    p = [1, *map(float, input().split())]
    for j in range(A+1):
        n *= p[j]
        m = min(m, s - n * t - 2 * j)
    print(f'Case #{i}: {m}')