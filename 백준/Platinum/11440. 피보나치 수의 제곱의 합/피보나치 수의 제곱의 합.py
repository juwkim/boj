def matrix_mul(a, b):
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
            res[i][j] %= mod
    return res

def fib(n):
    if n <= 1:
        return n

    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]

    while n > 0:
        if n % 2:
            ans = matrix_mul(ans, a)
        a = matrix_mul(a, a)
        n //= 2

    return ans[0][1]

mod = 1000_000_007
n = int(input())
print((fib(n)*fib(n+1)) % mod)