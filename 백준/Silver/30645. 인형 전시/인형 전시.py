R, C, N, *h = map(int, open(0).read().split())
A = [[0] * C for _ in range(R + 1)]
i, j = 1, 0
for num in sorted(h):
    if num > A[i - 1][j]:
        A[i][j] = num
        if j == C - 1:
            i += 1
            j = 0
        else:
            j += 1
        if (i, j) == (R + 1, 0):
            break
print((i - 1) * C + j)