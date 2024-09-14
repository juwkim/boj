N, M = map(int, input().split())
A = [[0] * M for _ in range(M)]
A[M - 1][0], A[M - 1][M - 1] = 1, 1
for i in range(M - 1):
    A[i][i + 1] = 1

mod = 1000000007

def mul(A, B):
    C = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            for k in range(M):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def pow(A, n):
    result = [[1 if i == j else 0 for j in range(M)] for i in range(M)]
    base = A
    while n > 0:
        if n % 2 == 1:
            result = mul(result, base)
        base = mul(base, base)
        n //= 2    
    return result

mat = pow(A, N - M + 1)
ans = sum(mat[-1]) % mod
print(ans)
