import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    if K == 1:
        if N > 3:
            print(*range(2, N + 1, 2), *range(1, N + 1, 2))
        else:
            print(-1)
    else:
        print(*range(1, N + 1))