import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, M, K = g()
    if K == 1 and N > M:
        ans = -1
    else:
        ans = 0
        while True:
            ans += 1
            N -= M * K
            if N <= 0:
                break
            ans += 1
            N += 1
    print(ans)