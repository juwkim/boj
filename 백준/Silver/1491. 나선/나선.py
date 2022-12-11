N, M = map(int, input().split())
p, q = min(N, M) >> 1, max(N, M)

if N >= M and M & 1:
    x, y = q - 1 - p, p
elif N & 1:
    if N < M:
        x, y = p, q - 1 - p
    else:
        x, y = p - 1, p
else:
    x, y = p - 1, p
print(x, y)