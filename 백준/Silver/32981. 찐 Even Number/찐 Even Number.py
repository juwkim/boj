import sys
input = sys.stdin.readline

m = 10**9 + 7
for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(5)
    else:
        print(4 * pow(5, N - 1, m) % m)