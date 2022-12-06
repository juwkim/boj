from math import gcd
A, B = map(int, input().split())
print(A*B//gcd(A, B))