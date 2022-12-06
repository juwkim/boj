import math
A, B = map(int, input().split())
k = math.gcd(A, B)
print(k, A*B//k, sep='\n')