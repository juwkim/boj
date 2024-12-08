def seive(n):
    A = [True] * (n + 1)
    A[0] = A[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if A[i]:
            for j in range(i * i, n + 1, i):
                A[j] = False
    return A

N = int(input())
if N == 1:
    B, S = 1, 0
else:
    p = seive(N)
    f, b = 'S', 'S'
    B, S = 0, 2
    for i in range(3, N + 1):
        if p[i]:
            if b == 'B':
                B -= 1
                S += 1
            S += 1
            f, b = 'S', f
        else:
            B += 1
            b = 'B'
print(B, S)