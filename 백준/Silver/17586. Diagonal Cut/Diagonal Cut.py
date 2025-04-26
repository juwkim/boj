import math

M, N = map(int, input().split())
g = math.gcd(M, N)
if M // g & 1 and N // g & 1:
    print(g)
else:
    print(0)