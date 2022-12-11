N, M = map(int, input().split())

if N & 1:
    if M & 1:
        if N < M:
            p = N // 2
            x, y = p, M - 1 - p
        else:
            p = M // 2
            x, y = N - 1 - p, p
    else:
        if N < M:
            p = N // 2
            x, y = p, M - 1 - p
        else:
            p = M // 2
            x, y = p - 1, p
else:
    if M & 1:
        if N < M:
            p = N // 2
            x, y = p - 1, p
        else:
            p = M // 2
            x, y = N - 1 - p, p
    else:
        p = min(N, M) // 2
        x, y = p - 1, p
            
print(x, y)