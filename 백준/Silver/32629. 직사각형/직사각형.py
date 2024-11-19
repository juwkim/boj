import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    P = int(N**.5)
    if N == P * P:
        print(4 * P)
    elif N <= P * (P + 1):
        print(4 * P + 2)
    else:
        print(4 * P + 4)