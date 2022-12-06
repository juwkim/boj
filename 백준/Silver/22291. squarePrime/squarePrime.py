from math import isqrt
def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
    

def isSquare(n):
    if n <= 0:
        return False
    s = isqrt(n)
    return s * s == n

def P2(A):
    n = len(A)
    ans = 0
    for i in range(2, n):
        if isSquare(A[i]) and isPrime(i):
            ans += A[i]
    return ans