from math import gcd

R, G = map(int, input().split())
l = gcd(R, G)
for i in range(1, int(l**.5) + 1):
    q, r = divmod(l, i)
    if r == 0:
        print(i, R // i, G // i)
        if i != q:
            print(q, R // q, G // q)