g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, K = g()
    if N == 1:
        print(K)
    else:
        r, q = divmod(K, 2 * N - 2)
        buf = [r] + [2 * r] * (N - 2) + [r]
        
        idx = 0
        direction = 0
        while q:
            buf[idx] += 1
            if idx in [0, N - 1]:
                direction ^= 1
            if direction == 1:
                idx += 1
            else:
                idx -= 1
            q -= 1
        print(*buf)