from math import gcd
for _ in range(int(input())):
    N = int(input())
    print(1, end=' ')
    for i in range(2, N):
        if gcd(N, i) == 1:
            print(i, end=' ')
    print()