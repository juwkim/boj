import math

def solve(n):
    t = (math.isqrt(8 * n + 1) - 1) // 2
    p = n - t * (t + 1) // 2
    return t * (t + 1) * (t + 2) // 3 + p * (p + 1) >> 1

A, B = map(int, input().split())
print(solve(B) - solve(A - 1))