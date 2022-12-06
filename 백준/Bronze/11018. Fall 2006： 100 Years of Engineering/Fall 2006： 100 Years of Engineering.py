g = 9.81
for i in range(1, 1 + int(input())):
    n, M = input().split()
    M = float(M)
    res = []
    for _ in range(int(n)):
        res.append([*map(float, input().split())])
        M += res[-1][0]
    h, v = 0, 0
    for m, t, f in res:
        a = f / M - g
        h += v * t + a * t * t / 2
        v += a * t
        M -= m
    print(f'Data Set {i}:\n{h:.2f}\n')