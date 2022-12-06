def gcd(A, B):
    if A == 0: return B
    return gcd(B%A, A)

n = int(input())
s = n // 2
while True:
    if gcd(s, n - s) == 1:
        print(s, n - s)
        break
    s -= 1