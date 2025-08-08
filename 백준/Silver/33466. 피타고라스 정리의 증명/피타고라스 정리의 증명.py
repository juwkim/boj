import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    print(2 * N - (N & 1))