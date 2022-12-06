def gcd(A, B):
    if A == 0: return B
    return gcd(B%A, A)

A, B = sorted(map(int, input().split()))
print('1'*gcd(A, B))