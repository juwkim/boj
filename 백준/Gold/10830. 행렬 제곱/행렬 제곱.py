input = __import__('sys').stdin.readline


def g(): return [*map(int, input().split())]

def matrix_mul(A, B):
    B_T = [*zip(*B)]
    C = [[sum(a * b for a, b in zip(A[i], B_T[j])) % mod for j in range(N)] for i in range(N)]
    return C

def solve(A, B):
    if B == 1:
        return A

    ans = solve(matrix_mul(A, A), B >> 1)
    if B&1:
        ans = matrix_mul(A, ans)
    return ans

mod = 1000
N, B = g()
A = [[num % mod for num in g()] for _ in range(N)]
ans = solve(A, B)

for line in ans:
    print(*line)