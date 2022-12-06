from math import gcd
for _ in range(int(input())):
    A, B = map(int, input().split())
    print(A*B//gcd(A, B))