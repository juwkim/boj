from math import gcd

for _ in range(int(input())):
    A, B, X = map(int, input().split())
    print(X // gcd(A, B))