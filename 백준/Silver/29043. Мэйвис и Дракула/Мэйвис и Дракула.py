import sys
input = sys.stdin.readline
from math import gcd

for _ in range(int(input())):
    A, B = map(int, input().split())
    ans = 0
    while True:
        g = gcd(A, B)
        ans = max(ans, A * B // g)
        if g == 1:
            break
        B -= 1
    print(ans)