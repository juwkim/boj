import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    print(((N >> K) + 1) >> 1)