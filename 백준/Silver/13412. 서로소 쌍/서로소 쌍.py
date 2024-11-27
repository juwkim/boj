import sys
input = sys.stdin.readline
from math import gcd

for _ in range(int(input())):
    N = int(input())
    ans = 0
    for A in range(1, int(N**0.5) + 1):
        B = N // A
        if A * B == N and gcd(A, B) == 1:
            ans += 1
    print(ans)