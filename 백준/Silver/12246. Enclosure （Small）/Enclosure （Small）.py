import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def empty_triangle(size):
    return size * (size + 1) // 2

for tc in range(1, 1 + int(input())):
    N, M, K = map(int, input().split())
    N, M = sorted([N, M])
    ans = K
    for R in range(2, N + 1):
        for C in range(max((K + R - 1) // R, R), M + 1):
            for i in range(R << 1):
                if sum(j//4 * (j//4 + 1) // 2 for j in range(i, i + 4)) > R * C - K:
                    ans = min(ans, 2 * (R + C - 2) - i + 1)
                    break
    print(f'Case #{tc}: {ans}')