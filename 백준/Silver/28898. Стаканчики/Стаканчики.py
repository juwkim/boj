import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = sorted(map(int, input().split()))
    ans = N * (N + 1) * (3 * M - N + 1) // 6
    print(ans)