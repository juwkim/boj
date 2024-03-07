import sys
g = lambda: map(int, sys.stdin.readline().split())

while True:
    X, Y, N = g()
    if X == 0:
        break
    r = bytearray(X + 1)
    c = bytearray(Y + 1)
    d1 = bytearray(X + Y + 1)
    d2 = bytearray(X + Y + 1)
    for _ in range(N):
        a, b = g()
        r[a] = 1
        c[b] = 1
        d1[a + b] = 1
        d2[a - b + Y] = 1
    ans = 0
    for i in range(1, X + 1):
        if r[i]:
            continue
        for j in range(1, Y + 1):
            if c[j] or d1[i + j] or d2[i - j + Y]:
                continue
            ans += 1
    print(ans)