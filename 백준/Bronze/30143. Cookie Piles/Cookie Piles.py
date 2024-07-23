import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, A, D = map(int, input().split())
    print(N * (2 * A + (N - 1) * D) // 2)