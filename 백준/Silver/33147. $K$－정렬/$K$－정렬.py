from math import gcd
N, K = map(int, input().split())
g = gcd(N, K)
if all((num - i) % g == 0 for i, num in enumerate(map(int, input().split()))):
    print("YES")
else:
    print("NO")